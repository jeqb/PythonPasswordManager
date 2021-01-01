from sqlalchemy import Column, Integer, String

from .Base import Base

class EncryptionCheck(Base):
    """
    The purpose of this table is to check whether the
    encryption key provided by the user is the one used
    to encrypt the data.

    There is a single column with the message
    """

    __tablename__ = 'EncryptionCheck'

    Id = Column(Integer, primary_key=True)
    EncryptionMessage = Column(String)