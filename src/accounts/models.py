from sqlalchemy import Column, Integer, String

from src.database import Base


class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
