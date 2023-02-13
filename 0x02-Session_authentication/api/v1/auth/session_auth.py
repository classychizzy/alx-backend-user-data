#!/usr/bin/env python3
""" a program that implements session auth
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ a class that implements session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ a function that creates a session """
        if user_id is None:
            return None

        if type(user_id) is not str:
            return None

        from uuid import uuid4
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
