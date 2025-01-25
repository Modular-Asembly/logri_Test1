from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.Comment import Comment
from app.modassembly.database.sql.get_sql_session import get_sql_session


def get_comments_for_tweet(tweet_id: int) -> List[Comment]:
    with get_sql_session() as session:
        comments = session.execute(
            select(Comment).where(Comment.tweet_id == tweet_id)
        ).scalars().all()
    return comments
