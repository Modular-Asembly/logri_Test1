from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base


class Follow(Base):
    __tablename__ = 'follows'

    follower_id: int = Column(Integer, ForeignKey('users.id'), primary_key=True)
    followed_id: int = Column(Integer, ForeignKey('users.id'), primary_key=True)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
