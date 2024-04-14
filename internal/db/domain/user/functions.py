# Добавление нового пользователя / обновление данных текущего
def set_group():
    c1 = User(
        id = message.from_user.id,
        group = ,
        created_at =
    )

    session.add(c1)

    session.commit()

def get_user_by_id():