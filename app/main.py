from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

from app.models.Follow import Follow
from app.models.Tweet import Tweet
from app.models.User import User
from app.models.Like import Like
from app.endpoints.register_user import router
app.include_router(router)
from app.endpoints.authenticate_user import router
app.include_router(router)
from app.endpoints.post_tweet import router
app.include_router(router)
from app.endpoints.view_tweets import router
app.include_router(router)
from app.endpoints.follow_unfollow_user import router
app.include_router(router)
from app.endpoints.like_tweet import router
app.include_router(router)

# Database

from app.modassembly.database.sql.get_sql_session import Base, engine
Base.metadata.create_all(engine)
