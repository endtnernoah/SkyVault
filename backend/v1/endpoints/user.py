from fastapi import APIRouter, HTTPException
from core.schemas import schema
from core.models.database import session, User
from core.crypt import context
import datetime

# Set up API Router
router = APIRouter()

@router.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate):
    try:
        new_user = schema.User(
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            password = context.crypt_context.hash(user.password),
            is_privileged = user.is_privileged,
            created_at = datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow()
        )

        session.add(new_user)
        session.commit()

        return new_user

    except Exception as ex:
        # Roll back the session and raise HTTPException
        session.rollback()
        raise HTTPException(status_code=500, details="Error creating user: " + str(ex))

@router.get("/users/", response_model=List[schema.User])
def get_all_users():
    try:
        users = session.query(User).all()

        return users
    except Exception as ex:
        raise HTTPException(status_code=500, details="Error getting all users: " + str(ex))

@router.get("/users/{user_id}", response_model=schema.User)
def get_user(user_id: str):
    try:
        user = session.query(User).get(user_id)

        return user
    except Exception as ex:
        raise HTTPException(status_code=500, details="Error getting user: " + str(ex))

@router.put("/users/{user_id}", response_model=schema.User)
def update_user(user_id: str, updated_user: schema.UserCreate):
    try:
        user = session.query(User).get(user_id)

        user.first_name = updated_user.first_name
        user.last_name = update_user.last_name
        user.email = updated_user.email
        user.password = context.crypt_context.hash(updated_user.password)
        user.is_privileged = updated_user.is_privileged
        user.updated_at = datetime.datetime.utcnow()

        session.commit()

        return user
    except:
        session.rollback()
        raise HTTPException(status_code=500, details="Error updating user: " + str(ex))

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    try:
        user = session.query(User).get(user_id)

        session.delete(user)
        session.commit()

        return None
    except:
        raise HTTPException(status_code=500, details="Error deleting user: " + str(ex))
