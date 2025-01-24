from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.follow.follow_user import follow_user
from app.services.follow.unfollow_user import unfollow_user

router = APIRouter()

class FollowUnfollowRequest(BaseModel):
    follower_id: int
    followed_id: int
    action: str  # "follow" or "unfollow"

class SuccessResponse(BaseModel):
    message: str

@router.post("/follow_unfollow", response_model=SuccessResponse)
def follow_unfollow_user(request: FollowUnfollowRequest) -> SuccessResponse:
    """
    Endpoint to follow or unfollow a user.

    - **follower_id**: ID of the user who wants to follow/unfollow.
    - **followed_id**: ID of the user to be followed/unfollowed.
    - **action**: "follow" to follow a user, "unfollow" to unfollow a user.

    Returns a success message upon completion.
    """
    if request.action == "follow":
        follow_user(request.follower_id, request.followed_id)
        return SuccessResponse(message="Successfully followed the user.")
    elif request.action == "unfollow":
        unfollow_user(request.follower_id, request.followed_id)
        return SuccessResponse(message="Successfully unfollowed the user.")
    else:
        raise HTTPException(status_code=400, detail="Invalid action. Use 'follow' or 'unfollow'.")
