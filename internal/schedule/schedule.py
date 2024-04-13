from datetime import datetime


class Schedule:
    def __init__(self, data: dict):
        pass

    # Проверка существования группы
    def group_exist(self, group_number: str) -> bool:
        pass

    def get_schedule(self, group_number: str, date):
        # Расписание может отличаться
        if not self.group_exist(group_number):
            return None

        # Структуру ниже нужно возвращать в виде data класса
        # LOOK https://habr.com/ru/articles/415829/
        return {
            "schedule": {
                "groupNumber": "303-31м",  # Номер группы
                "currentDate": datetime.now(),
                "dayWeek": 0,   # 0 - пн, 6 - вс
                "weekType": 0,  # 0 - числитель, 1 - знаменатель
                "date": date,   # Дата на которую сгенерировано расписание
                "lessons": [
                    {
                        "type": "lesson",  # lesson - информация о занятии, window - окно
                        "number": 1,  # Номер пары
                        "info": "История и методология биологии (пр), ЭОиДОТ",  # Описание
                        "time": {
                            "from": "10:00",  # Со скольки
                            "to": "11:20"  # До скольки
                        },
                        "current": False,  # Идет ли сейчас эта пара
                    },
                    {
                        "type": "window",  # lesson - информация о занятии, window - окно
                        "number": 2,  # Номер пары
                        "info": "",  # Описание
                        "time": {  # эти параметры определяет timetable
                            "from": "10:00",  # Со скольки
                            "to": "11:20"  # До скольки
                        },
                        "current": False,  # Идет ли сейчас эта пара
                    },
                    {
                        "type": "lesson",  # lesson - информация о занятии, window - окно
                        "number": 3,  # Номер пары
                        "info": "Современная систематика живых организмов (пр). А628,623//ФТД: Этология (пр), А623",  # Описание
                        "time": {
                            "from": "10:00",  # Со скольки
                            "to": "11:20"  # До скольки
                        },
                        "current": False,  # Идет ли сейчас эта пара
                    },
                ]
            }
        }