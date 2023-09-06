from fastapi import APIRouter
from core.schemas import user

router = APIRouter()


@router.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate):

    u = user.User()

    return u