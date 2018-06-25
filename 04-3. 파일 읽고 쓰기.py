for i in range(1,11) :
    data = '%d줄입니다'%i
    print(data)

# w 쓰기 모드
f = open('New.txt', 'w')
for i in range(1,11) :
    data = '%d줄입니다\n'%i
    f.write(data)
f.close()

# r 읽기 모드
# readline 첫째줄을 불러온다
f = open('New.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('New.txt', 'r')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()

# readlines 모든 줄을 한줄씩 불러온다
f = open('New.txt', 'r')
lines = f.readlines()
for line in lines :
    print(line)
f.close()

# read 파일 전체를 불러온다
f = open('New.txt', 'r')
data = f.read()
print(data)
f.close()

# a 추가 모드
f = open('New.txt', 'a')
for i in range(11, 21) :
    data = '%d줄입니다\n'%i
    f.write(data)
f.close()

# with 파일 자동으로 닫는다
with open('foo.txt', 'w') as f:
    f.write('Life is short, you need python')

#Q1
f1 = open('test1.txt','w')
f1.write('Life is too short')
f1.close()
f2 = open('test1.txt','r')
print(f2.read())

#Q2
a = input('저장할 내용을 입력하세요 = ')
f = open('test2.txt','a')
f.write(a)
f.write('\n')
f.close()

#Q3
with open('abc.txt','w') as f :
    f.write('AAA\nBBB\nCCC\nDDD\nEEE')

f = open('abc.txt','r')
lines = f.readlines()
f.close()

rlines = reversed(lines)
f = open('abc.txt','w')
for line in rlines :
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

#Q4
with open('test4.txt','w') as f :
    f.write('Life is too short\nYou need java')

f = open('test4.txt','r')
data = f.read()
data1 = data.replace('java','python')
f.close()

f = open('test4.txt','w')
f.write(data1)
f.close()

#Q5
with open('sample.txt','w') as f :
    f.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100')

f = open('sample.txt','r')
data = f.readlines()
f.close()

f = open('result.txt','w')
sum = 0
for i in data :
    score = int(i)
    sum += score
avg = sum / int(len(data))
f.write(str(avg))
f.close()

