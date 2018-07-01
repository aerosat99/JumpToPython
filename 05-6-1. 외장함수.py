import sys
sys.path
sys.path.append("C:/Users/JIEUN/Documents/Python/JumpToPython/mymod")

import pickle
f = open('test.txt', 'wb')
data = {1 : 'python', 2 : 'you need'}
pickle.dump(data, f)
f.close()

f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)
f.close()

import os
print(os.environ)
print(os.environ['PATH'])
print(os.chdir('C:/Users/JIEUN/Documents/Python/JumpToPython'))
print(os.getcwd())
print(os.system('dir/w'))
g = os.popen('dir')
print(g.read())

import shutil
f = open('bbb.txt', 'w')
f.write('Revolution')
f.close()
shutil.copy('bbb.txt','ccc.txt')
h = open('ccc.txt', 'r')
h1 = h.read()
print(h1)
h.close()

import glob
print(glob.glob('C:/Users/JIEUN/Documents/Python/JumpToPython/0*'))
# 경로명에서 대소문자 지켜야 한다

import tempfile
filename = tempfile.mkdtemp()
print(filename)
j = tempfile.TemporaryFile()
f.close()
print(j)

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x', (time.localtime(time.time())))) # %x = MM/DD/YY
print(time.strftime('%c', (time.localtime(time.time()))))

for i in range(10) :
    print(i)
    time.sleep(0.5)   # 0.5초 간격으로 결과 출력

import calendar
print(calendar.calendar(2018))
print(calendar.prcal(2018))
print(calendar.prmonth(2018,12))

print(calendar.weekday(2018,11,24))  # 월요일부터 0, 5는 토요일
print(calendar.monthrange(2018,2)) # 2018년 2월 1일은 목요일, 마지막날은 28일
