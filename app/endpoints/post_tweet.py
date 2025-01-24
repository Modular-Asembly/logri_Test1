from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.services.tweet.add_tweet_to_db import add_tweet_to_db

router = APIRouter()

class TweetRequest(BaseModel):
    user_id: int
    content: str

class TweetResponse(BaseModel):
    message: str

@router.post("/tweet", response_model=TweetResponse, status_code=status.HTTP_201_CREATED)
def post_tweet(tweet_data: TweetRequest) -> TweetResponse:
    """
    Endpoint to post a new tweet.

    - **user_id**: The ID of the user posting the tweet.
    - **content**: The content of the tweet.

    Returns a success message upon successful tweet creation.
    """
    if not tweet_data.content.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tweet content cannot be empty.")

    add_tweet_to_db(user_id=tweet_data.user_id, content=tweet_data.content)
    return TweetResponse(message="Tweet posted successfully.")
