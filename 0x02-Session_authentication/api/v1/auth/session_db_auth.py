#!/usr/bin/env python3
"""Module for session authentication using database"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Database session authentication class"""

    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession
        and returns the Session ID"""

        session_id = super().create_session(user_id)
        if not session_id:
            return None
        kwargs = {
            "user_id": user_id,
            "session_id": session_id
        }
        user = UserSession(**kwargs)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user_id in the database based on session_id
        """
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            for id in user_id:
                return id.to_json().get('id')
        return None

    def destroy_session(self, request=None):
        """
        destroys the UserSession based on the Session ID from the request cookie
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return None

        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            for session in user_session:
                session.remove()
                return True
        return False
