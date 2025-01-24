from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base


class Tweet(Base):
    __tablename__ = 'tweets'

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    content: str = Column(String, nullable=False)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
