import bcrypt
from typing import Union


def hash_password(plain_password: Union[str, bytes]) -> bytes:
    """
    Takes a plain text password as input and returns a hashed version of the password.

    :param plain_password: The plain text password to hash.
    :return: The hashed password.
    """
    # Ensure the password is in bytes
    if isinstance(plain_password, str):
        plain_password_bytes = plain_password.encode('utf-8')
    else:
        plain_password_bytes = plain_password

    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password_bytes, salt)
    return hashed_password
