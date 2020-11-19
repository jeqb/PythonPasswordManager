from sqlalchemy import Column, Integer, String

from .Base import Base

class Note(Base):
    __tablename__ = 'Note'

    Id = Column(Integer, primary_key=True)
    Content = Column(String)