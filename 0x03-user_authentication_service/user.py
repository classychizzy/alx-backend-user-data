#!/usr/bin/env python3
""" model for a user """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# declarative base class
Base = declarative_base()


# an example mapping using the base
class User(Base):
    """ User class """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
