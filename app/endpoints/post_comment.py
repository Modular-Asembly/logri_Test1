from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.comment.add_comment_to_db import add_comment_to_db

router = APIRouter()

class CommentRequest(BaseModel):
    user_id: int
    tweet_id: int
    content: str
    parent_comment_id: Optional[int] = None

class CommentResponse(BaseModel):
    message: str

@router.post("/comments", response_model=CommentResponse)
def post_comment(comment: CommentRequest) -> CommentResponse:
    """
    Endpoint to post a comment on a tweet.

    - **user_id**: ID of the user making the comment.
    - **tweet_id**: ID of the tweet being commented on.
    - **content**: Content of the comment.
    - **parent_comment_id**: (Optional) ID of the parent comment if this is a reply.
    """
    if not comment.content.strip():
        raise HTTPException(status_code=400, detail="Comment content cannot be empty.")

    add_comment_to_db(
        user_id=comment.user_id,
        tweet_id=comment.tweet_id,
        content=comment.content,
        parent_comment_id=comment.parent_comment_id
    )

    return CommentResponse(message="Comment posted successfully.")
