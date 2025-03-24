from sqladmin import Admin, ModelView
from fastapi import FastAPI
from db import engine
from .model import User
from blog.model import Blogs


from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn


# Define the ModelView for the User model
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]

class PostAdmin(ModelView, model=Blogs):
    column_list = [Blogs.id, Blogs.title, Blogs.content,Blogs.image,Blogs.status]