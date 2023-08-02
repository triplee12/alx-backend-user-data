#!/usr/bin/env python3
"""Regex-ing."""

import re


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    """
    Return the log message obfuscated.

    Args:
        fields (list): a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
        fields in the log line (message)
    Return:
        String: the log message obfuscated
    """
    return re.sub(r"(?<=^|{sep})({fields})(?={sep}|$)".format(fields='|'.join(
        map(re.escape, fields)), sep=re.escape(separator)),
        redaction, message
    )
