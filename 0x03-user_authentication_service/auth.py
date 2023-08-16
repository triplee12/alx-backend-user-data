#!/usr/bin/env python3
"""Hash password."""

from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash password."""
    encode_pwd = password.encode(encoding='UTF-8', errors='strict')
    hash_pwd = hashpw(password=encode_pwd, salt=gensalt())
    return hash_pwd


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the authentication."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_password = _hash_password(password=password)
            new_user = self._db.add_user(
                email=email, hashed_password=hash_password
            )
            return new_user
