from sqlalchemy import Column, ForeignKey,Integer,String,LargeBinary,Enum
from sqlalchemy.orm import relationship
from db import Base,engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    username = Column(String,unique=True,index=True)
    email= Column(String,unique=True,index=True)
    blogs = relationship("Blogs", back_populates= "author")
    
Base.metadata.create_all(bind=engine)