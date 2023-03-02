#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    """Uses hashpw to encrypt password"""
    return bcrypt.hashpw(b'password', bcrypt.gensalt())
