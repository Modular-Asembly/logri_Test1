from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.modassembly.database.sql.get_sql_session import Base


class Comment(Base):
    __tablename__ = "comments"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    tweet_id: int = Column(Integer, ForeignKey("tweets.id"), nullable=False)
    parent_comment_id: int = Column(Integer, ForeignKey("comments.id"), nullable=True)
    content: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="comments")
    tweet = relationship("Tweet", back_populates="comments")
    parent_comment = relationship("Comment", remote_side=[id], back_populates="replies")
    replies = relationship("Comment", back_populates="parent_comment")

