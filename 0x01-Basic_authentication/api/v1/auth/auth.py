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
        a function that requires auth
        """
        return False

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
