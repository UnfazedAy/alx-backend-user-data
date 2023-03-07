#!/usr/bin/env python3
"""The basic authentication module"""

from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple
import base64


class BasicAuth(Auth):
    """Basic Authentication class that inherits from Auth"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        returns the Base64 part of the
        Authorization header for a Basic Authentication:
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        A method that returns the decoded value of Base64
        string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            auth_token = base64.b64decode(base64_authorization_header)
            return auth_token.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        A method that returns the user email and
        password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header.split(":")[1]

        return email, password
