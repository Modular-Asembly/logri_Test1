from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.tweet.add_tweet_to_db import add_tweet_to_db
from app.services.tweet.count_user_tweets_today import count_user_tweets_today
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class TweetRequest(BaseModel):
    user_id: int
    content: str

class TweetResponse(BaseModel):
    message: str

@router.post("/tweet", response_model=TweetResponse)
def post_tweet(tweet_data: TweetRequest, db: Session = Depends(get_sql_session)) -> TweetResponse:
    """
    Endpoint to post a tweet.

    - **user_id**: ID of the user posting the tweet.
    - **content**: Content of the tweet.
    """
    # Validate tweet content length
    if len(tweet_data.content) == 0:
        raise HTTPException(status_code=400, detail="Tweet content cannot be empty.")
    
    # Check the user's tweet count for the day
    tweet_count = count_user_tweets_today(tweet_data.user_id)
    if tweet_count >= 100:
        raise HTTPException(status_code=400, detail="Tweet limit reached for today.")

    # Add tweet to the database
    add_tweet_to_db(tweet_data.user_id, tweet_data.content, db)

    return TweetResponse(message="Tweet posted successfully.")
