from sqlalchemy import Column, Integer, String

from .Base import Base

class Entry(Base):
    __tablename__ = 'Entry'

    Id = Column(Integer, primary_key=True)
    Username = Column(String)
    Email = Column(String)
    Password = Column(String)
    Category = Column(String)
    Note = Column(String)