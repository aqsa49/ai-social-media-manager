from sqlalchemy import Column,Integer,String
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    content = Column(String)
    status = Column(String, default="scheduled")
