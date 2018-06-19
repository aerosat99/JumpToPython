#1
print('점프 투 파이썬 문제를 풀어보자')

#2
print('Life is too short\nYou need Python')
print('''
Life is too short
You need Python''')

#3
a = 'PYTHON'
print(' '* 24 + a)  #문자열 더하기 + 기능

#4
pin = '881120-1068234'
birthday = pin[:6]
print(birthday)
idn = pin[7:]
print(idn)

#5
sex = pin[7]
print(sex)

#6
str1 = '1980M1120'
print(str1[4] + str1[:4] + str1[5:])

#7
a = 'PYTHON'
print(' '* 24 + a)
print('%30s'%a)

#8
b = 'Life is too short, You need python'
print(b.index('short'))

#9
str2 = 'a:b:c:d'
print(str2.replace(':', '#'))

#10
str3 = str2.split(':')
print(str3)
str4 = '#'.join(str3)
print(str4)              # join을 이용한 문자열 삽입은 문자열 뿐만 아니라 리스트에도 사용 가능하다.