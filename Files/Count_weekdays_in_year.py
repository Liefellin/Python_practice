# Zala Weyker
# 12/28/2023
# Count weekdays in year
# Counts the number of times a given weekday appears in a given year (ie. how many thursdays in 2044)

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday_constant):
        wdaysinyear = 0
        for month in range(1, 13):
            for day in self.itermonthdays2(year, month):
                if day[0] and day[1] == weekday_constant:
                    wdaysinyear += 1
        return wdaysinyear


a = MyCalendar()

print(a.count_weekday_in_year(2000, 6))
