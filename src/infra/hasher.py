import hashlib
import json


class HashCalculator:
    @staticmethod
    def compute(header: dict, body: dict) -> str:
        canonical = json.dumps(
            {"header": header, "body": body},
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()