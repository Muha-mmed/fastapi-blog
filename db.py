from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///db.sql"

engine = create_engine(DATABASE_URL)
local_session = sessionmaker(bind=engine,autoflush=False)
Base = declarative_base()

def get_db():
    db = local_session()
    try:
      yield db
    finally:
      db.close()