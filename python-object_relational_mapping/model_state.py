#!/usr/bin/python3
"""Defines the State model and the declarative Base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A state stored in the table states."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
