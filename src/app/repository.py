from abc import ABC, abstractmethod
from typing import Any


class ProblemRepo(ABC):
    @abstractmethod
    def create(
        self,
        hash: str,
        header: dict[str, Any],
        body: dict[str, Any],
    ) -> None:
        pass