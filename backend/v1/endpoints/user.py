from fastapi import APIRouter
from core.schemas import schema

router = APIRouter()


@router.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate):

    u = user.User()

    return u
