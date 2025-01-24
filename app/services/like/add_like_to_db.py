from sqlalchemy.orm import Session
from app.models.Like import Like
from app.modassembly.database.sql.get_sql_session import get_sql_session


def add_like_to_db(user_id: int, tweet_id: int) -> None:
    with next(get_sql_session()) as db:  # type: Session
        like = Like(user_id=user_id, tweet_id=tweet_id)
        db.add(like)
        db.commit()
