from db import Base,engine
from sqlalchemy import Column, ForeignKey,Integer,String,LargeBinary,Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import DateTime


from utils import STATUS



class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(225))
    content= Column(String)
    image = Column(String,nullable=True)
    author_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"))
    slug = Column(String(255), unique=True)
    status = Column(Enum(STATUS,native_enum=False),server_default=STATUS.draft)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    
    comments = relationship("Comment", back_populates="blog", cascade="all, delete")
    author = relationship("User",back_populates="blogs")
    
    
class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    content= Column(String)
    email = Column(String)    
    blog_id = Column(Integer, ForeignKey('blogs.id', ondelete="CASCADE"))
    parent_id = Column(Integer, ForeignKey('comments.id', ondelete="CASCADE"), nullable=True)
    replies = relationship("Comment", backref="parent", remote_side="Comment.id", cascade="all, delete")

    blog = relationship("Blogs", back_populates="comments")


Base.metadata.create_all(bind=engine)
