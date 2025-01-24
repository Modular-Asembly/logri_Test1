from sqlalchemy.orm import Session
from app.models.User import User
from app.modassembly.database.sql.get_sql_session import get_sql_session


def add_user_to_db(username: str, email: str, password_hash: str) -> None:
    with next(get_sql_session()) as db:  # type: Session
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        db.add(new_user)
        db.commit()
