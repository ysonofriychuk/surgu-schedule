import json
import pprint
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
    currentDate: str
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
        # Расписание может отличаться
        if not self.group_exist(group_number):
            return None

        date_times = datetime.strptime(date, "%d-%m-%Y-%H-%M")
        dayWeek = date_times.weekday()

        week_number = date_times.isocalendar()[1]
        weekType = 0
        if week_number % 2 == 0:
            weekType = 1

        lesson = []

        times = date_times.time()
        num = self.data[group_number][day[dayWeek]].keys()

        min_num_lesson = float("inf")
        max_num_lesson = 0

        for num in self.data[group_number][day[dayWeek]]:
            try:
                num = int(num)
                min_num_lesson = min(int(num), min_num_lesson)
                max_num_lesson = max(int(num), max_num_lesson)
            except:
                pass

        for i in range(min_num_lesson, max_num_lesson+1):
            info = self.data[group_number][day[dayWeek]].get(str(i), "")

            time = get_lesson_time(info, i)

            time1 = datetime.strptime(time.from1, "%H-%M")
            time2 = datetime.strptime(time.to, "%H-%M")
            cur = False

            if time1.time() <= times <= time2.time():
                cur = True

            c = Lesson('lesson' if info else 'window', i, info, str(time), cur)
            lesson.append(c)

        schedule = ScheduleClass(groupNumber=group_number, currentDate=str(datetime.now()), dayWeek=dayWeek, weekType=weekType,
                                 date=date, lessons=lesson)
        return schedule


if __name__ == "__main__":
    with open('schedule.json', "r", encoding='utf-8') as file:
        configuration = json.load(file)

    sh = Schedule(configuration)

    pprint.pprint(sh.get_schedule("102-03", '30-04-2024-17-30'))
