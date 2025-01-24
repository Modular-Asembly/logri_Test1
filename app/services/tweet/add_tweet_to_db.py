from sqlalchemy.orm import Session
from app.models.Tweet import Tweet
from app.modassembly.database.sql.get_sql_session import get_sql_session


def add_tweet_to_db(user_id: int, content: str) -> None:
    with next(get_sql_session()) as db:  # type: Session
        new_tweet = Tweet(user_id=user_id, content=content)
        db.add(new_tweet)
        db.commit()
