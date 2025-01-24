import os
import jwt
from datetime import datetime, timedelta
from typing import Dict, Union

def issue_auth_token(user_id: int) -> str:
    """
    Issues a JWT token for the user.

    :param user_id: The ID of the user for whom the token is issued.
    :return: A JWT token as a string.
    """
    secret_key = os.environ["JWT_SECRET_KEY"]
    algorithm = os.environ.get("JWT_ALGORITHM", "HS256")
    expiration_minutes = int(os.environ.get("JWT_EXPIRATION_MINUTES", "30"))

    payload: Dict[str, Union[str, int]] = {
        "user_id": str(user_id),
        "exp": int((datetime.utcnow() + timedelta(minutes=expiration_minutes)).timestamp())
    }

    token: str = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token
