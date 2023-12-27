# Zala Weyker
# 11/27/2023
# This program will create a datetimeobject for November 4, 2020, 14:53:00. it will then call the strf method to print:

# 2020/11/04 14:53:00
# 20/November/04 2:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

import datetime as dt

ourdate = dt.datetime(2020, 11, 4, 14, 53)

print(ourdate.strftime("%Y/%m/%d %H:%M:%S"))
print(ourdate.strftime("%y/%B/04 %I:%M:%S PM"))
print(ourdate.strftime("%a, %Y %b %d"))
print(ourdate.strftime("%A, %Y %B %d"))
print(ourdate.strftime("Weekday: %w"))
print(ourdate.strftime("Day of the year: %j"))
print(ourdate.strftime("Week number of the year: %W"))
