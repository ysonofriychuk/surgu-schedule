# TODO SURGU-010

# user_id
# group
# created_at
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
# class DB(Base):
#     __tablename__ = 'groups'
#     id = Column(Integer, primary_key=True)
#     group = Column(String(100), nullable=False)
#     created_at = Column(DateTime(), default=datetime.now)
#
#     __table_args__ = (
#         ForeignKeyConstraint(['user_id'], ['users.id']),
#         Index('title_content_index' 'title', 'content'),  # composite index on title and content
#     )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    group = Column(String(100), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
