import json
from typing import Any

import flask
import flask_restful
from flask import request

from src.app.exceptions import RepositoryError
from src.app.service import AbstractProblemService
from src.infra.mongo import MongoDriver
from src.infra.reader import ProblemReaderImpl
from src.infra.repository import ProblemRepoImpl
from src.infra.hasher import HashCalculator


class ProblemService(AbstractProblemService):
    def __init__(self) -> None:
        mongo = MongoDriver()
        collection = mongo.get_collection()
        self.repo = ProblemRepoImpl(collection)
        self.read = ProblemReaderImpl(collection)
        self.hash = HashCalculator()

    def create_problem(self) -> tuple[dict[str, Any], int]:
        header_raw = request.headers.get("X-Request-Header")
        if not header_raw:
            return {"message": "Отсутствует X-Request-Header"}, 400

        try:
            header = json.loads(header_raw)
        except json.JSONDecodeError:
            return {"message": "Некорректный JSON в X-Request-Header"}, 400

        if not isinstance(header, dict):
            return {"message": "Header должен быть объектом"}, 400

        try:
            body = request.get_json(force=True)
        except Exception:
            return {"message": "Некорректный JSON в теле"}, 400

        if not isinstance(body, dict):
            return {"message": "Body должен быть объектом"}, 400

        h = self.hash.compute(header, body)
        try:
            self.repo.create(h, header, body)
        except RepositoryError as e:
            flask_restful.abort(500, message=str(e))

        return {"hash": h}, 201

    def find_problems(self) -> flask.Response:
        filters = flask.request.get_json(force=True)
        if not isinstance(filters, dict):
            flask_restful.abort(400, message="Фильтры должны быть JSON-объектом")

        try:
            docs = self.read.find(filters)
        except RepositoryError as e:
            flask_restful.abort(500, message=str(e))

        results = [
            {
                "id": str(d["_id"]),
                "hash": d["hash"],
                "header": d["header"],
                "body": d["body"],
            }
            for d in docs
        ]

        resp = flask.make_response(flask.jsonify(results), 200)
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return resp

    def find_by_hash(self) -> flask.Response:
        h = flask.request.args.get("h")
        if not h:
            flask_restful.abort(400, message="Не задан параметр hash")

        try:
            docs = self.read.find_by_hash(h)
        except RepositoryError as e:
            flask_restful.abort(500, message=str(e))

        results = [
            {
                "id": d["_id"],
                "hash": d["hash"],
                "header": d["header"],
                "body": d["body"],
            }
            for d in docs
        ]
        return flask.jsonify(results)