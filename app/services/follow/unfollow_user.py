from sqlalchemy.orm import Session
from app.models.Follow import Follow
from app.modassembly.database.sql.get_sql_session import get_sql_session


def unfollow_user(follower_id: int, followed_id: int) -> None:
    with next(get_sql_session()) as db:  # type: Session
        follow_entry = db.query(Follow).filter(
            Follow.follower_id == follower_id,
            Follow.followed_id == followed_id
        ).first()

        if follow_entry:
            db.delete(follow_entry)
            db.commit()
