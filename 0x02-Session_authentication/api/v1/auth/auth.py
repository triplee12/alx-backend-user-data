#!/usr/bin/env python3
"""Auth class."""

from flask import request
from os import getenv
from typing import List, TypeVar


class Auth:
    """ Authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication."""
        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        has_wildcard = any(x.endswith("*") for x in excluded_paths)
        if not has_wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if e.endswith("*"):
                if path.startswith(e[:-1]):
                    return False
            if path == e:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header."""
        if request:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user."""
        return None

    def session_cookie(self, request=None):
        """Session cookie."""
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookies.get(session_name, None)
