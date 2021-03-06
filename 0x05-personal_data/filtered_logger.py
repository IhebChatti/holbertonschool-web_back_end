#!/usr/bin/env python3
"""[filter_datum]
"""

from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """[RedactingFormatter initialization]

        Args:
            fields (List[str]): [fields]
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """[format]

        Args:
            record (logging.LogRecord): [LogRecord]

        Returns:
            str: [formatted str]
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """[get_logger]

    Returns:
        logging.Logger: [logging Logger]
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """[filter_datum]

    Args:
        fields (List[str]): [all fields to obfuscate]
        redaction (str): [what the field will be obfuscated]
        message (str): [the log line]
        separator (str): [which character is separating all fields]

    turns:
        str: [message]
    """
    for field in fields:
        message = re.sub('{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message


def get_db() -> mysql.connector.connection.MySQLConnection:
    """[get_db]

    Returns:
        mysql.connector.connection.MySQLConnection: [mysql connection]
    """
    db_user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None)
    db_pw = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME', None)

    return mysql.connector.connect(user=db_user,
                                   password=db_pw,
                                   host=db_host,
                                   database=db_name)


def main():
    pass

if __name__ == "__main__":
    main()
