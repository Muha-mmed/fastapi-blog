from db import Base,engine
from sqlalchemy import Column,Integer,String,LargeBinary,Enum
from sqlalchemy.orm import relationship

from utils import STATUS

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    content= Column(String)
    email = Column(String)
    
      
class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String)
    content= Column(String)
    image = Column(String,nullable=True)
    status = Column(Enum(STATUS,native_enum=False),server_default=STATUS.draft)
    # comment = relationship(Comment,back_populates="blog")
    
    

    # blog = relationship(Blogs,back_populates="comment")

Base.metadata.create_all(bind=engine)
