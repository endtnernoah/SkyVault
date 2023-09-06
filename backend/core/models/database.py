from sqlalchemy import create_engine, Column, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from core.settings import database_url
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, comment="Hashed")
    is_privileged = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_login = Column(DateTime)

    # Relationship with passwords table
    passwords = relationship("Password", back_populates="user")

class Password(Base):
    __tablename__ = 'passwords'

    id = Column(UUID, primary_key=True)
    content = Column(String, nullable=False, comment="Encrypted")
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    username = Column(String, nullable=True)
    url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationship with users table
    user = relationship("User", back_populates="passwords")

# Create an engine and bind it to the Base
engine = create_engine(database_url)
Base.metadata.create_all(engine)

# Create a session and bind it to the engine
Session = sessionmaker(bind=engine)
session = Session()

