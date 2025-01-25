from typing import Optional
from sqlalchemy.orm import Session

from app.models.Comment import Comment
from app.modassembly.database.sql.get_sql_session import get_sql_session


def add_comment_to_db(user_id: int, tweet_id: int, content: str, parent_comment_id: Optional[int] = None) -> None:
    with get_sql_session() as session:
        comment = Comment(
            user_id=user_id,
            tweet_id=tweet_id,
            content=content,
            parent_comment_id=parent_comment_id
        )
        session.add(comment)
        session.commit()
