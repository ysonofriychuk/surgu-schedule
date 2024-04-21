import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from internal.schedule.timetable import get_lesson_time


@dataclass
class Lesson:
    type: str
    number: int
    info: str
    time: get_lesson_time(type, number)
    current: bool


@dataclass
class ScheduleClass:
    groupNumber: str
    currentDate = datetime.now()
    dayWeek: int
    weekType: int
    date: str
    lessons: List[Lesson] = field(default_factory=list)


class Schedule:
    def __init__(self, data: dict):
        self.data = data

    # Проверка существования группы
    def group_exist(self, group_number: str) -> bool:
        return group_number.lower() in self.data

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
                "dayWeek": 0,  # 0 - пн, 6 - вс
                "weekType": 0,  # 0 - числитель, 1 - знаменатель
                "date": date,  # Дата на которую сгенерировано расписание
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
                ]
            }
        }


if __name__ == "__main__":
    with open('schedule.json', "r", encoding='utf-8') as file:
        configuration = json.load(file)

    sh = Schedule(configuration)
