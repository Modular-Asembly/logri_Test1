from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.services.like.add_like_to_db import add_like_to_db
from app.services.tweet.update_like_count import update_like_count

router = APIRouter()

class LikeRequest(BaseModel):
    user_id: int
    tweet_id: int

class LikeResponse(BaseModel):
    message: str

@router.post("/like", response_model=LikeResponse, status_code=status.HTTP_200_OK)
def like_tweet(like_request: LikeRequest) -> LikeResponse:
    """
    Endpoint to like a tweet.

    - **user_id**: The ID of the user liking the tweet.
    - **tweet_id**: The ID of the tweet to be liked.

    Returns a success message upon successful liking of the tweet.
    """
    try:
        add_like_to_db(like_request.user_id, like_request.tweet_id)
        update_like_count(like_request.tweet_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return LikeResponse(message="Tweet liked successfully.")
