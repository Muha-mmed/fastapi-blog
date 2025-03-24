from blog.routes import router
from fastapi import FastAPI
from sqladmin import Admin
from db import engine
from admin.admin import UserAdmin,PostAdmin

# FastAPI instance
app = FastAPI()
# Include routes from blog
app.include_router(router)

# Initialize SQLAdmin
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)