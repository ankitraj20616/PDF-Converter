from database import Base
from sqlalchemy import Column, String, Integer

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, autoincrement= True)
    username = Column(String(255), unique = True)
    email = Column(String(255), unique = True)
    password = Column(String(255))
