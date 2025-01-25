from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.comment.get_comments_for_tweet import get_comments_for_tweet
from app.models.Comment import Comment

router = APIRouter()

class CommentResponse(BaseModel):
    id: int
    user_id: int
    tweet_id: int
    parent_comment_id: Optional[int]
    content: str
    created_at: str

@router.get("/tweets/{tweet_id}/comments", response_model=List[CommentResponse])
def fetch_comments(tweet_id: int) -> List[CommentResponse]:
    """
    Fetch comments for a specific tweet.

    - **tweet_id**: The ID of the tweet for which to fetch comments.
    """
    comments = get_comments_for_tweet(tweet_id)
    if not comments:
        raise HTTPException(status_code=404, detail="No comments found for this tweet.")
    
    return [
        CommentResponse(
            id=comment.id,
            user_id=comment.user_id,
            tweet_id=comment.tweet_id,
            parent_comment_id=comment.parent_comment_id,
            content=comment.content.__str__(),
            created_at=comment.created_at.isoformat()
        )
        for comment in comments
    ]
