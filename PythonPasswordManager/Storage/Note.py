from sqlalchemy import Column, Integer, String

from .Base import Base

class Note(Base):
    __tablename__ = 'Note'

    # internal
    Id = Column(Integer, primary_key=True)
    Salt = Column(String)