"""Defines various utilities that will be used in our code."""
import uuid


def generate_uuid():
    """Utility generates UUID string"""
    return str(uuid.uuid4())
