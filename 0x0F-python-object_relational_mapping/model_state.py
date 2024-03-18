#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class inherits from Base class containing the metadata object
    The newly created table object is intended to be accessed directly for
    MetaData-specific operations
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
