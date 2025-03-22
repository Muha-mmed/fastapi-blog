from fastapi import APIRouter,Depends, Form, HTTPException,File,UploadFile
from blog.schema import Blogs, CommentSchema,UpdateBlog
from db import get_db
from sqlalchemy.orm import Session
from blog.core import create_comment, delete_blog_svc, publish_post, create_post,draft_post,trashed_blogs,trash_blog_svc, update_blog_svc
from utils import CreateStatus


router = APIRouter()
    
    
@router.post("/")
async def create(title:str=Form(...),content:str=Form(...),image:UploadFile = File(...),status:CreateStatus=Form(...),db:Session=Depends(get_db)):
    blog_data = {"title":title,"content":content,"status":status}
    blog = create_post(blog_data,image,db) 
    return {"status": "successful", "data": blog}

@router.get("/published")
async def get_published_post(db:Session=Depends(get_db)):
    blog = publish_post(db) 
    return blog

@router.get("/draft")
def get_draft_post(db:Session= Depends(get_db)):
    drafts = draft_post(db)
    return drafts

@router.get("/trash")
def trash_post(db:Session = Depends(get_db)):
    drafts = trashed_blogs(db)
    return drafts

@router.put("/update_post/{post_id}")
def update_blog(post_id:int,blog:UpdateBlog,db:Session=Depends(get_db)):
    trash = update_blog_svc(post_id,blog,db)
    return {"message":trash}

@router.delete("/delete/{post_id}")
def delete_blog(post_id:int,db:Session=Depends(get_db)):
    post = delete_blog_svc(post_id,db)
    if not post:
        raise HTTPException(status_code=404,detail="no post with such id")
    return {"message": f"post with id ({post_id}) deleted successfully"}


@router.post("/comment")
def comment(post_id:int,comment:CommentSchema,db:Session = Depends(get_db)):
    com = create_comment(post_id,comment,db)
    return com
