from typing import Optional
from pydantic import BaseModel

from utils import STATUS,CreateStatus

class Blogs(BaseModel):    
    title: str
    content: str
    status: CreateStatus
    slug:str
    
    class Config:
        from_attribute = True
        
class UpdateBlog(BaseModel):    
    title: Optional[str] = None
    content: Optional[str] = None
    status: Optional[STATUS] = None
    
    class Config:
        from_attribute = True
        
class CommentSchema(BaseModel):
    content: str
    email: str
    
class UpdateCommentSchema(BaseModel):
    content: Optional[str] = None