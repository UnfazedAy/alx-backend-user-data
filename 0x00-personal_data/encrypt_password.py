#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    """Uses hashpw to encrypt password"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pw = bcrypt.hashpw(bytes, salt)
    return hash_pw

    """In 1 line. I prefer the first though"""
    # return bcrypt.hashpw(b'password', bcrypt.gensalt())
