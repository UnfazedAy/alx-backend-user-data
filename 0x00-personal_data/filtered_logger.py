#!/usr/bin/env python3
"""A module for filtering logs"""

from typing import List
import re


# Start of task 0
def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    A function that uses regex to replace occurences of certain
    field values and returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
