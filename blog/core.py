from sqlalchemy.orm import Session,joinedload

from fastapi import File, HTTPException,UploadFile

from blog.model import Blogs, Comment
from blog.schema import Blogs as blogSchema,CommentSchema, UpdateBlog


def create_post(blog:blogSchema,image: UploadFile, db:Session):
    blog = Blogs(
        title = blog["title"],
        content = blog["content"],
        image= image.filename,
        status = blog["status"]
    )
    if not blog:
        raise HTTPException(details='heyyy')

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def update_blog_svc(post_id:int,blog:UpdateBlog,db:Session):
    post = db.query(Blogs).filter(Blogs.id == post_id).first()
    if not post:
        return "invalid post id"
    update_data = blog.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(post, key, value)
        
    db.commit()
    db.refresh(post)
    return post

def delete_blog_svc(post_id:int,db:Session):
    post = db.query(Blogs).filter(Blogs.id == post_id).first()
    if not post:
        return {"message":"invalid post id"}
    db.delete(post)
    db.commit()
    return {"message":"blog deleted successfully"}

def publish_post(db:Session):
    blog = db.query(Blogs).options(joinedload(Blogs.comments)).filter(Blogs.status == "publish").all()
    if blog == []:
        return {"message":"no publish post"}
    return blog

def draft_post(db:Session):
    draft = db.query(Blogs).options(joinedload(Blogs.comments)).filter(Blogs.status == "draft").all()
    if not draft:
        return  {"message":"draft page is empty"}
    return draft

def trashed_blogs(db:Session):
    trash = db.query(Blogs).options(joinedload(Blogs.comments)).filter(Blogs.status == "trash").all()
    if not trash:
        return  {"message":"trash page is empty"}
    return trash

def trash_blog_svc(post_id:int,db:Session):
    post = db.query(Blogs).filter(Blogs.id == post_id).first()
    if not post:
        return "invalid post id"
    move_to_trash = post.status = "trash"
    return {"message":"post moved to trash",}

def create_comment(post_id:int,comment:CommentSchema,db:Session):
    post = db.query(Blogs).filter(Blogs.id == post_id)
    if not post:
        return {"message":"post not found"}
    com = Comment(
        content = comment.content,
        email = comment.email,
        blog_id = post_id
    )
    db.add(com)
    db.commit()
    db.refresh(com)
    return "comment successfully"