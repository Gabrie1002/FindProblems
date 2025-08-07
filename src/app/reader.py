from abc import ABC, abstractmethod
from typing import Any


class ProblemReader(ABC):
    @abstractmethod
    def find(
        self,
        filters: dict[str, Any],
    ) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def find_by_hash(
        self,
        hash: str,
    ) -> list[dict[str, Any]]:
        pass