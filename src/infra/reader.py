from typing import Any

from pymongo.errors import PyMongoError
from pymongo.collection import Collection

from src.app.exceptions import RepositoryError
from src.app.reader import ProblemReader


class ProblemReaderImpl(ProblemReader):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection

    def find(self, filters: dict[str, Any]) -> list[dict[str, Any]]:
        clauses: list[dict[str, Any]] = []
        for k, v in filters.items():
            sval = str(v)
            clauses.append(
                {
                    "$or": [
                        {f"header.{k}": sval},
                        {f"body.{k}": sval},
                    ]
                }
            )
        query: dict[str, Any] = {"$and": clauses} if clauses else {}
        try:
            cursor = self.collection.find(query)
        except PyMongoError as e:
            raise RepositoryError(
                f"Failed to find problems: {e}"
            ) from e

        return list(cursor)

    def find_by_hash(self, h: str) -> list[dict[str, Any]]:
        try:
            cursor = self.collection.find({"hash": h})
        except PyMongoError as e:
            raise RepositoryError(
                f"Failed to find by hash: {e}"
            ) from e

        return list(cursor)