from typing import List
from sqlalchemy.orm import Session
from app.models.Tweet import Tweet
from app.models.Follow import Follow
from app.modassembly.database.sql.get_sql_session import get_sql_session


def get_user_feed(user_id: int) -> List[Tweet]:
    with get_sql_session() as session:
        # Query to find all users that the given user follows
        followed_users = session.query(Follow.followed_id).filter(Follow.follower_id == user_id).subquery()

        # Query to get tweets from followed users
        tweets = session.query(Tweet).filter(Tweet.user_id.in_(followed_users)).order_by(Tweet.created_at.desc()).all()

    return tweets
