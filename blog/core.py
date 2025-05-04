from sqlalchemy.orm import Session,joinedload

from fastapi import File, HTTPException,UploadFile

from blog.model import Blogs, Comment
from blog.schema import Blogs as blogSchema,CommentSchema, UpdateBlog,UpdateCommentSchema

def get_blog(post_id,db:Session):
    return db.query(Blogs).filter(Blogs.id == post_id).first()

def get_comment(comment_id,db):
    return db.query(Comment).filter(Comment.id == comment_id).first()
    
def create_post(blog:blogSchema,image: UploadFile, db:Session):
    blog = Blogs(
        title = blog["title"],
        content = blog["content"],
        image= image.filename,
        status = blog["status"],
        slug = blog["slug"]
    )
    if not blog:
        raise HTTPException(details='blog not found',status_code=404)

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def update_blog_svc(post_id:int,blog:UpdateBlog,db:Session):
    post = get_blog(post_id,db)
    if not post:
        return "invalid post id"
    update_data = blog.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(post, key, value)
        
    db.commit()
    db.refresh(post)
    return post

def delete_blog_svc(post_id:int,db:Session):
    post = get_blog(post_id,db)
    if not post:
        return None
    db.delete(post)
    db.commit()
    db.refresh(post)

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
    post = get_blog(post_id,db)
    if not post:
        return {"message":"invalid post id"}
    post.status = "trash"
    db.commit()  # Commit changes to database
    db.refresh(post) 
    return {"message":"post moved to trash"}

def create_comment(post_id:int,comment:CommentSchema,db:Session):
    post = get_blog(post_id,db)
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

def delete_comment_svc(comment_id:int,email:str,db:Session):
    comment = get_comment(comment_id,db)
    if not comment:
        return {"message":"invalid comment id"}
    email = db.query(Comment).filter(Comment.email == email).first()
    if not email:
        return {"message":"you're not the owner of the comment"}
    db.delete(comment)
    db.commit()
    return {"message":"comment deleted"}

def update_comment_svc(comment_id:int,email:str,comment:UpdateCommentSchema,db:Session):
    com = get_comment(comment_id,db)
    if not com:
        return {"message":"invalid comment id"}
    email = db.query(Comment).filter(Comment.email == email).first()
    if not email:
        return {"message":"you're not the owner of the comment"}
    new_comment = comment.model_dump(exclude_unset=True)
    for key,value in new_comment.items():
        setattr(com,key,value)
    db.commit()
    db.refresh(com)
    return com