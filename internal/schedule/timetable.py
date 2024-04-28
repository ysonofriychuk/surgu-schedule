# расписание звонков для основных занятий
import re

BASE_TIMETABLE = {
    '1': ('08-30', '09-50'),
    '2': ('10-00', '11-20'),
    '3': ('11-30', '12-50'),
    '4': ('13-20', '14-40'),
    '5': ('14-50', '16-10'),
    '6': ('16-20', '17-40'),
    '7': ('18-00', '19-20'),
    '8': ('19-30', '20-50')
}

# расписание звонков для занятий по ФК
PHYSICAL_TIMETABLE = {
    '1': ("09-00", "10-20"),
    '2': ('10-30', '11-50'),
    '3': ('12-00', '13-20'),
    '4': ('13-30', '14-50'),
    '5': ('15-00', '16-25'),
    '6': ('16-30', '17-50')
}
# Определяет какое время занятий, для физ-ры одно расписание, для прочих - другое
from dataclasses import dataclass


@dataclass
class Data:
    from1: str
    to: str


def get_lesson_time(lesson: str, number: int):
    from1 = BASE_TIMETABLE[str(number)][0]
    to = BASE_TIMETABLE[str(number)][1]
    if re.fullmatch(r".*культур\D и спорт.*", lesson):
        from1 = PHYSICAL_TIMETABLE[str(number)][0]
        to = PHYSICAL_TIMETABLE[str(number)][1]
    time = Data(from1, to)
    return time