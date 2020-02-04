import time
import datetime

class ClockIterator:
    ''' Class to implement an infinite clock '''

    def __init__(self):
        self.hr_max = 23
        self.min_max = 59
        self.sec_max = 59
    
    def __iter__(self):
        self.hr = datetime.datetime.now().hour
        self.min = datetime.datetime.now().minute
        self.sec = datetime.datetime.now().second
        return self
    
    def __next__(self):
        if self.sec < self.sec_max:
            self.sec += 1
        if self.min < self.min_max and self.sec == self.sec_max:
            self.min += 1
            self.sec = 0
        if self.min == self.min_max and self.sec == self.sec_max:
            self.hr += 1
            self.min = 0
            self.sec = 0
        if self.hr == self.hr_max and self.min == self.min_max and self.sec == self.sec_max:
            self.hr = 0
            self.min = 0
            self.sec = 0

        def formatter(n):
            n = str(n)
            if len(n) != 2:
                return "{}{}".format(0, n)
            else:
                return n

        result = ("{}:{}:{}").format(formatter(self.hr), formatter(self.min), formatter(self.sec))
        time.sleep(1)
        return result

if __name__ == "__main__":
    for i in ClockIterator():
        print(i)
