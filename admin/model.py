from sqlalchemy import Column, ForeignKey,Integer,String,LargeBinary,Enum

from db import Base,engine


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    username = Column(String,unique=True,index=True)
    email= Column(String,unique=True,index=True)
    
Base.metadata.create_all(bind=engine)