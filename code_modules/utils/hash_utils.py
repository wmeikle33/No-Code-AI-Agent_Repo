
import hashlib


def sha256_hash(content: str) -> str:
    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()


def md5_hash(content: str) -> str:
    return hashlib.md5(
        content.encode("utf-8")
    ).hexdigest()


def content_fingerprint(content: str) -> str:
    return sha256_hash(content)
