# https://pythonru.com/biblioteki/vvedenie-v-sqlalchemy
# Добавление нового пользователя / обновление данных текущего
import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()

# Модель пользователя
class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    group = Column(String(100))
    created_at = Column(DateTime(), default=datetime.datetime.now)


engine = create_engine("sqlite:///sqlite3.db")
Base.metadata.create_all(engine)


def set_group(user_id: int, group: str):
    session = Session(bind=engine)

    user: User = session.query(User).get(user_id)

    if user is None:
        user = User(
            user_id=user_id,
            group=group
        )
    else:
        user.group = group

    session.add(user)
    session.commit()


if __name__ == "__main__":
    set_group(1, "606-11")
    set_group(2, "501")
    set_group(1, "606-12")
