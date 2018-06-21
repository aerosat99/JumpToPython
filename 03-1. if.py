score = 70
if score >= 60 :
    message = 'success'
else :
    message = 'failure'
print(message)

message = 'success' if score >= 60 else 'failure'
print(message)

#Q1
money = 5000
card = 0
if money >= 4000 or card :
    print('Taxi')
else :
    print('Taxi No')

#Q2
lucky_list = [1,9,23,46]
hold = 22
print('Wow') if hold in lucky_list else print(';;')

#Q3
a = int(input('int = '))
print('Even') if a % 2 == 0 else print('Odd')

#Q4
a = "age : 30, Height : 180"
b = a.split(',')
print(b)
c = b[0].split(':')[-1]
d = b[1].split(':')[-1]
age = int(c)
height = int(d)
print('Yes') if age < 30 and height >= 175 else print('No')

#Q5
a = "Life is too short, you need python"
if 'wife' in a:  # False
    print('wife')
elif 'python' in a and 'you' not in a:  # False
     print('python')
elif 'shirt' not in a:  # True # 가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"만 출력된다.
    print('shirt')
elif 'need' in a:  # True # True이지만 출력되지 않는디.
    print('need')
else:
    print('none')