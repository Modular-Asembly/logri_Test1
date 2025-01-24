from sqlalchemy.orm import Session
from app.models.Follow import Follow
from app.modassembly.database.sql.get_sql_session import get_sql_session


def follow_user(follower_id: int, followed_id: int) -> None:
    with next(get_sql_session()) as db:  # type: Session
        follow = Follow(follower_id=follower_id, followed_id=followed_id)
        db.add(follow)
        db.commit()
