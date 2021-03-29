#!/usr/bin/env python3
"""[filter_datum]
"""

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """[filter_datum]

    rgs:
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
