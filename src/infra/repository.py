from typing import Any

from pymongo.errors import PyMongoError
from pymongo.collection import Collection

from src.app.exceptions import RepositoryError
from src.app.repository import ProblemRepo


class ProblemRepoImpl(ProblemRepo):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection

    def create(
        self,
        hash: str,
        header: dict[str, Any],
        body: dict[str, Any],
    ) -> None:
        doc = {"hash": hash, "header": header, "body": body}
        try:
            self.collection.insert_one(doc)
        except PyMongoError as e:
            raise RepositoryError(
                f"Failed to insert problem: {e}"
            ) from e