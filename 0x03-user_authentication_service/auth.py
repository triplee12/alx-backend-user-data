#!/usr/bin/env python3
"""Hash password."""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hash password."""
    encode_pwd = password.encode(encoding='UTF-8', errors='strict')
    hash_pwd = hashpw(password=encode_pwd, salt=gensalt())
    return hash_pwd
