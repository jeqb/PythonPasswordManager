from sqlalchemy import Column, Integer, String

from .Base import Base

class Entry(Base):
    __tablename__ = 'Entry'

    # internal
    Id = Column(Integer, primary_key=True)
    Salt = Column(String)

    # external
    Username = Column(String)
    Email = Column(String)
    Password = Column(String)
    Category = Column(String)
    Note = Column(String)