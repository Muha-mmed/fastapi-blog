from db import Base,engine
from sqlalchemy import Column, ForeignKey,Integer,String,LargeBinary,Enum
from sqlalchemy.orm import relationship

from utils import STATUS



class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String)
    content= Column(String)
    image = Column(String,nullable=True)
    status = Column(Enum(STATUS,native_enum=False),server_default=STATUS.draft)
    comments = relationship("Comment", back_populates="blog", cascade="all, delete")
    
class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    content= Column(String)
    email = Column(String)    
    blog_id = Column(Integer, ForeignKey('blogs.id', ondelete="CASCADE"))
    
    blog = relationship("Blogs", back_populates="comments")



Base.metadata.create_all(bind=engine)
