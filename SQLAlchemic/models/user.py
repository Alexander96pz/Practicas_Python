# from config.bd import meta,engine
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    name=Column(String(50),nullable=False)
    apellido=Column(String(50), nullable=False)

# Base.metadata.create_all(engine)

