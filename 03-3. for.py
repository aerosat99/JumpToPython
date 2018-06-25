a = [(1,2), (3,4),(5,6)]
for (s, l) in a :
    print(s+l)

marks = [90,25,67,45,80]
candidate=[]
for a in marks :
    if a >= 60 :
        candidate.append(a)
print(len(candidate))

number = 0
for mark in marks :
    number += 1
    if mark >= 60 :
        print('%d번 학생은 합격입니다'%number)
    else :
        print('%d번 학생은 불합격입니다' %number)

number = 0
for mark in marks :
    number += 1
    if mark < 60 : continue # 60점 이하면 continue에 걸려서 처음으로 돌아간다
    print('%d번 학생은 합격입니다. 축하합니다'%number) # 60점 이상이면 continue에 걸리지 않아 합격 메시지 뜬다

sum = 0
for i in range(1,11) :
    sum += i
print(sum)

marks = [90,25,67,45,80]
for number in range(len(marks)) : # range(len(marks)) = range(0, 5) = 0,1,2,3,4
    if marks[number] < 60 : continue
    print('%d번 학생은 합격입니다. 축하합니다'%(number+1))

for i in range(2,10) :
    for j in range(1,10) :
        print(i * j, end = '')
    print('')

a = [1,2,3,4]
result =[]
for num in a :
    result.append(num*3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

#Q1
for i in range(1,101) :
    print(i)

#Q2
sum = 0
for a in range(1,1001) :
    if a % 5 == 0 :
        sum += a
print(sum)

#Q3
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for a in A :
    sum += a
print(sum/int(len(A)))

#Q4
data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in data:
    if blood_type in result:  # 키 값이 존재하는 경우에는 기존 값에 더함
        result[blood_type] += 1
    else:  # 키 값이 없는 경우에는 새로운 키 생성
        result[blood_type] = 1
print(result)

#Q5
numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

#Q6
sentence = 'Life is too short, you need python'
ex = 'aeiou'
print(''.join([a for a in sentence if a not in ex]))