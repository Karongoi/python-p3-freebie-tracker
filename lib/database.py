# lib/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///freebie.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
