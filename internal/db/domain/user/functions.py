# Добавление нового пользователя / обновление данных текущего
from sqlalchemy.orm import Session

from internal.db.db import engine
from internal.db.entity.user import User

session = Session(bind=engine)

def set_group():
    user = User(
        user_id = ,
        group =
    )
    session.add(user)
    session.commit()