#5-6-1
import sys
sys.path.append("C:/Users/JIEUN/Documents/Python/JumpToPython/mymod")

#5-6-2
import os
print(os.system('dir'))
os.chdir("C:/Users/JIEUN/Documents/Python/JumpToPython")
result = os.popen("dir")
print(result.read())

#5-6-3
import glob
b = list(glob.glob("C:/Users/JIEUN/Documents/Python/JumpToPython/*.py"))
print(b)

#5-6-4
import time
date = time.strftime('%Y/%m/%d %H/%M/%S', time.localtime(time.time()))
print(date)
date2 = time.strftime('%Y/%m/%d %H/%M/%S')
print(date2)

#5-6-5
import random

result = []
while len(result) <  6 :
    j = random.randint(1,45)   # 난수 발생
    if j not in result :      # 중복되지 않도록 리스트에 넣는다
        result.append(j)
print(result)

#5-6-6
from collections import namedtuple
Student = namedtuple('Student', ['name', 'score'])
a = Student(name = "홍길동", score = 30)
print(a.name)
print(a.score)
