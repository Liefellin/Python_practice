# Zala Weyker
# 9/29/2023
# Days of the week
# Keeps track of the days of the week

class WeekDayError(Exception):
    def __init__(self):
        super().__init__()


class Weeker:
    __weekdays = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    __rweekdays = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

    def __init__(self, __day):
        if __day in list(Weeker.__weekdays.values()):
            self.__day = Weeker.__rweekdays[__day]
        else:
            raise WeekDayError

    def __str__(self):
        return Weeker.__weekdays[self.__day]

    def add_days(self, n):
        self.__day += n
        if self.__day > 6:
            self.__day %= 7

    def subtract_days(self, n):
        self.__day -= n
        while self.__day < 0:
            self.__day += 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
