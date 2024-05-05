import hashlib


class HashService:
    @staticmethod
    def hash_string(string: str) -> str:
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
