import random
a = random.random()
print(a)

b = random.randint(1,10)
print(b)

def random_pop(data) :
    number = random.randint(0., len(data)-1)
    return data.pop(number)

if __name__ == "__main__" :
    data = [1,2,3,4,5]
    while data : print(random_pop(data))

def random_pop(data) :
    number = random.choice(data)
    data.remove(number)
    return number
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
random.shuffle(data)
print(data)
random.shuffle(data)
print(data)

# namedtuple
a = ('홍길동', 25, 'programmer')
b = ('김철수', 30, 'manager')
c = ('김영희', 42, 'designer')
for person in [a,b,c] :
    print('이름 : %s' % person[0])
    print('나이 : %s' % person[1])
    print('직업 : %s' % person[2])

class Person :
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
a = Person(name="홍길동", age=25, job="Programmer")
b = Person(name="김철수", age=32, job="Manager")
c = Person(name="김영희", age=41, job="Designer")
for person in [a, b, c]:
    print("이름:%s" % person.name)
    print("나이:%s" % person.age)
    print("직업:%s" % person.job)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'job'])
a = Person(name="홍길동", age=25, job="Programmer")
b = Person(name="김철수", age=32, job="Manager")
c = Person(name="김영희", age=41, job="Designer")
for person in [a, b, c]:
    print("이름:%s" % person.name)
    print("나이:%s" % person.age)
    print("직업:%s" % person.job)

f = 'Life is short, you need python'
d1 = dict()
for c in f :
     if c in d1 :
         d1[c] += 1
     else :
         d1[c] = 1
d1.items()
print(d1)

from collections import defaultdict
f = 'Life is short, you need python'
d2 = defaultdict(int)
for c in f :
    d2[c] += 1
d2.items()
print(d2)

s = [('a', 100), ('b', 200), ('c', 300), ('a', 150), ('c', 120)]
d3 = defaultdict(list)
for k, v in s:
    d3[k].append(v)
d3.items()
print(d3)
