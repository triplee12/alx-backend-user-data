#!/usr/bin/env python3

"""Session Data Base Authentication module."""

from api.v1.auth.session_exp_auth import SessionExpAuth
from os import getenv
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session Data Base Authentication class."""

    def create_session(self, user_id=None):
        """Create session."""
        if user_id:
            session_id = super().create_session(user_id)
            if not session_id:
                return
            new_user = UserSession(user_id=user_id, session_id=session_id)
            new_user.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """User id for session id."""
        if not session_id:
            return
        try:
            us_list = UserSession.search({session_id: session_id})
            for us in us_list:
                created_at = us.get('created_at', None)
                if not created_at:
                    return
                if (datetime.now() > created_at +
                        timedelta(seconds=self.session_duration)):
                    return
                return us.get('user_id', None)
        except Exception:
            return

    def destroy_session(self, request=None) -> bool:
        """Destroy session."""
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if super().destroy_session(request):
                    try:
                        us_list = UserSession.search({session_id: session_id})
                        for us in us_list:
                            us.remove()
                            return True
                    except Exception:
                        return False
        return False
