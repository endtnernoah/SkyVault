from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Database Model for the User.
    """
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True, nullable=False)
    last_name = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, unique=True, index=True, nullable=False)
    is_privileged = Column(Boolean, default=False, unqiue=False, index=True, nullable=False)