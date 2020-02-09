import time

class ClockIterator:
    ''' Class to implement an infinite clock '''

    def __init__(self):
        self.min_max = 23
        self.sec_max = 60
    
    def __iter__(self):
        self.min = 0
        self.sec = 0
        return self
    
    def __next__(self):
        def formatter(n):
            n = str(n)
            if len(n) != 2:
                return "{}{}".format(0, n)
            else:
                return n

        result = ("{}:{}").format(formatter(self.min), formatter(self.sec))

        if self.sec < self.sec_max:
            self.sec += 1
        if self.min < self.min_max and self.sec == self.sec_max:
            self.min += 1
            self.sec = 0
        if self.min == self.min_max and self.sec == self.sec_max:
            self.min = 0
            self.sec = 0
        if  self.min == self.min_max and self.sec == self.sec_max:
            self.min = 0
            self.sec = 0
        return result

    def user_iter(self, num):
        arr = []

        for i in self:
            arr.append(i)
            if len(arr) == num:
                break
        
        return arr[-1]

if __name__ == "__main__":
    
    #for i in ClockIterator():
    #    print(i)

    print(ClockIterator().user_iter(1))
