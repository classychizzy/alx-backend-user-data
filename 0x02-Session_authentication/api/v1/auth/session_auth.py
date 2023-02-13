#!/usr/bin/env python3
""" a program that implements session auth
"""
from api.v1.auth.auth import Auth
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ a function that creates user_id for a session
        """
        if session_id is None:
            return None

        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ current user """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ destroys a session"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
