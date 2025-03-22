
from enum import Enum


class STATUS(str,Enum):
    publish = "publish"
    draft = "draft"
    trash = "trash"
    
class CreateStatus(str,Enum):
    publish = "publish"
    draft = "draft"