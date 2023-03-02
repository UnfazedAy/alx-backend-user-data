#!/usr/bin/env python3
"""A module for filtering logs"""

from typing import List
import logging
import os
import mysql.connector
import re


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


# start of task 1
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )


# Start of task 2
def get_logger() -> logging.Logger:
    """creates a logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


# start of task 3
def get_db() -> mysql.connector.connection.MySQLConnection:
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_passwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")

    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_passwd,
        database=db_name
    )
