#!/usr/bin/python3
"""Module for user session model"""

from models.base import Base


class UserSession(Base):
    """User session class"""

    def __init__(self, *args: list, **kwargs: dict) -> None:
        """Initialize user session instances"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
