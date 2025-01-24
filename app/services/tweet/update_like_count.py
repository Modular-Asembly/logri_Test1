from sqlalchemy.orm import Session
from app.models.Tweet import Tweet
from app.modassembly.database.sql.get_sql_session import get_sql_session


def update_like_count(tweet_id: int) -> None:
    with next(get_sql_session()) as session:  # type: Session
        tweet = session.query(Tweet).filter(Tweet.id == tweet_id).first()
        if tweet:
            tweet.like_count = (tweet.like_count or 0) + 1
            session.commit()
