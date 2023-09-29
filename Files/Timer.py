# Zala Weyker
# 9/28/2023
# Timer Class
# A standrd military clock that can be manually ticked up or down. rollover occurs at maximum or minimum.

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        # Write code here
        #

    def __str__(self):
        h = str(self.hours)
        m = str(self.minutes)
        s = str(self.seconds)
        if len(h) < 2:
            h = "0" + h
        if len(m) < 2:
            m = "0" + m
        if len(s) < 2:
            s = "0" + s
        return f"{h}:{m}:{s}"
        # Write code here
        #

    def next_second(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < 24:
                    self.hours += 1
                else:
                    self.hours = 0

    def prev_second(self):
        if self.seconds > 0:
            self.seconds -= 1
        else:
            self.seconds = 59
            if self.minutes > 0:
                self.minutes -= 1
            else:
                self.minutes = 59
                if self.hours > 0:
                    self.hours -= 1
                else:
                    self.hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
