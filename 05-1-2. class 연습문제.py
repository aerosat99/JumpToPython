#5-1-1
class Calculator :
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

cal = Calculator()
cal.add(3)
cal.add(4)
print(cal.value)

#5-2-2
class Calculator :
    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

cal = Calculator(0)
cal.add(3)
cal.add(4)
print(cal.value)

#5-1-3
class Calculator :
    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator) :
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator(0)
cal.add(10)
cal.minus(7)
print(cal.value)

#5-1-4
class Calculator :
    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator) :
    def add(self, val):
        self.value += val
        if self.value >= 100 :
            self.value = 100

cal = MaxLimitCalculator(0)
cal.add(50)
cal.add(60)
print(cal.value)

#5-1-5
class Calculator :
    def __init__(self, list):
        self.list = list

    def sum(self):
        result = 0
        for a in self.list :
            result += a
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.list)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

import sys
print(sys.path)