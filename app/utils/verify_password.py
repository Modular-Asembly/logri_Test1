import bcrypt
from typing import Union


def verify_password(plain_password: str, hashed_password: Union[bytes, str]) -> bool:
    """
    Verifies if the plain text password matches the hashed password.

    :param plain_password: The plain text password to verify.
    :param hashed_password: The hashed password to compare against.
    :return: True if the passwords match, False otherwise.
    """
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)
