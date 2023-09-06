from pydantic import BaseModel

class UserBase(BaseModel):
    """
        User Base Model.
    """
    email: str
    password: str

class UserCreate(UserBase):
    """ 
        User Creation Model.
    """
    first_name: str
    last_name: str
    is_privileged: str

class User(UserBase):
    """ 
        User Model.
    """
    id: str

    class Config:
        """
            ORM enabled by default.
        """
        orm_mode = True
