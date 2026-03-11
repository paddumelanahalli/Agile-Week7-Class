# test_security.py
import pytest
from security import validate_password

def test_password_length():
# This WILL fail because 'validate_password' isn't written!
    assert validate_password("1234567") == False
    assert validate_password("12345678") == True

def test_password_digit_requirement():
    # NEW requirement tests
    assert validate_password("Password") == False
    assert validate_password("Password1") == True


# security.py
def validate_password(password):
    assert isinstance(password, str), "QA Error: Input must be a string"
    # Rule 1: minimum length
    long_enough = len(password) >= 8

    # Rule 2: must contain at least one number
    has_number = any(char.isdigit() for char in password)

    return long_enough and has_number
