##### 클래스 생성
class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second

    def sum(self) :
        result = self.first + self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()

a.setdata(4,2)
b.setdata(3,7)

print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())

##### 클래스 생성 - Constructor
class FourCal :
    def __init__(self, first, second) :
        self.first = first
        self.second = second

    def sum(self) :
        result = self.first + self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result

a = FourCal(4,2)
b = FourCal(3,7)

print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())

##### 클래스 생성 - 상속
class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
b = MoreFourCal(3,7)

print(a.pow())
print(b.pow())

##### 클래스 생성 - 상속 - overriding
class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())

###### 클래스의 활용
class Data :
    def __init__(self, data) :
        tmp = data.split('|')
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]
    def print_age(self):
        print(self.name)
    def print_grade(self):
        print('%s님 당신의 점수는 %s입니다'%(self.name, self.grade))

g = Data('홍길동|42|A')
g.print_age()
g.print_grade()