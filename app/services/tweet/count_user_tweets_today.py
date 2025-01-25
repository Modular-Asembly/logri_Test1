from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import Tweet
from app.modassembly.database.sql.get_sql_session import get_sql_session

def count_user_tweets_today(user_id: int) -> int:
    with next(get_sql_session()) as session:  # type: Session
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)

        tweet_count = session.query(Tweet).filter(
            Tweet.user_id == user_id,
            Tweet.created_at >= today_start,
            Tweet.created_at < today_end
        ).count()

    return tweet_count
