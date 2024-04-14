# https://pythonru.com/biblioteki/vvedenie-v-sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# class Post(Base):
#     __tablename__ = 'groups'
#     id = Column(Integer, primary_key=True)
#     group = Column(String(100), nullable=False)
#     created_at = Column(DateTime(), default=datetime.now)


