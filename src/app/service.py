from abc import ABC, abstractmethod
from typing import Any

import flask


class AbstractProblemService(ABC):
    @abstractmethod
    def create_problem(self) -> tuple[dict[str, Any], int]:
        pass

    @abstractmethod
    def find_problems(self) -> flask.Response:
        pass

    @abstractmethod
    def find_by_hash(self) -> flask.Response:
        pass