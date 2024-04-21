import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from internal.schedule.timetable import get_lesson_time
day = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'сб']


@dataclass
class Lesson:
    type: str
    number: int
    info: str
    time: str
    current: bool


@dataclass
class ScheduleClass:
    groupNumber: str
    currentDate = str
    dayWeek: int
    weekType: int
    date: str
    lessons: list


class Schedule:
    def __init__(self, data: dict):
        self.data = data

    # Проверка существования группы
    def group_exist(self, group_number: str) -> bool:
        return group_number.lower() in self.data

    def get_schedule(self, group_number: str, date):
        # Структуру ниже нужно возвращать в виде data класса
        # LOOK https://habr.com/ru/articles/415829/
        # Расписание может отличаться
        if not self.group_exist(group_number):
            return None

        date_strings = date[:10]
        date_times = datetime.strptime(date_strings, "%d-%m-%Y")
        dayWeek = date_times.weekday()
        lesson = []

        for i in self.data[group_number][day[dayWeek]]:
            les = Lesson('', i, self.data[group_number][day[dayWeek]][i], )
            print(self.data[group_number][day[dayWeek]][i])


if __name__ == "__main__":
    with open('schedule.json', "r", encoding='utf-8') as file:
        configuration = json.load(file)

    sh = Schedule(configuration)

    sh.get_schedule("304-21", '22-04-2024-11-30')
