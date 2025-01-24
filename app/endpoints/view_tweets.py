from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from app.services.feed.get_user_feed import get_user_feed
from app.models.Tweet import Tweet

router = APIRouter()

class TweetResponse(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: str

@router.get("/feed/{user_id}", response_model=List[TweetResponse])
def view_tweets(user_id: int) -> List[TweetResponse]:
    """
    Endpoint to view a user's tweet feed.

    :param user_id: The ID of the user whose feed is to be viewed.
    :return: A list of tweets from users that the given user follows.
    """
    tweets = get_user_feed(user_id)
    if not tweets:
        raise HTTPException(status_code=404, detail="No tweets found for this user feed.")
    
    return [TweetResponse(
        id=tweet.id,
        user_id=tweet.user_id,
        content=tweet.content.__str__(),
        created_at=tweet.created_at.isoformat()
    ) for tweet in tweets]
