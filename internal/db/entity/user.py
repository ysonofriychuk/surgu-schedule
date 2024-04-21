# TODO SURGU-010

# user_id
# group
# created_at

# Добавление нового пользователя / обновление данных текущего
import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Модель пользователя
class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    group = Column(String(100), default=0)
    created_at = Column(DateTime(), default=datetime.now)
