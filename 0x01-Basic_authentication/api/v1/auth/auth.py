#!/usr/bin/env python3
"""authentication module"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Class to handle user authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method for require auth"""
        return False


    def authorization_header(self, request=None) -> str:
        """A method to authorize the header requests"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """current user method"""
        return None