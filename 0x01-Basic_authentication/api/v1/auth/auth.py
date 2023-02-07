#!/usr/bin/env python3
"""
a module that handles authentication
"""

import requests
from typing import List, TypeVar


class Auth():
    """
    a class that handles authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        a function that defines what requires authentication
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or "{}/".format(path) in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path[-1] == "/":
                continue
            if path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ a function that authorizes the request header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        a function that checks for the instance of the current
        user
        """
        return None
