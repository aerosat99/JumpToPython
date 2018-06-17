# %d 정수 %s 문자열 %f 소수

# 숫자를 넢고 싶은 자리에 %d를 넣고 맨뒤 % 뒤에 해당 숫자를 넣으면 된다.
print("I eat %d Apples." %3)

# 문자를 넢고 싶은 자리에 %s를 넣고 맨뒤 % 뒤에 해당 문자를 넣으면 된다.
print("I eat %s Apples." %'five')

# 숫자, 문자를 변수로 처리해도 가능
number1 = 3
print("I eat %d Apples." %number1)
number2 = 'five'
print("I eat %s Apples." %number2)

number3 = 10
day = 'three'
print('I ate %d apple. So I was sick for %s days.' %(number3, day))

# %s 뭐든지 넣을 수 있는데 문자열로 바꿔서 들어간다
print('I have %s apples.' %3)
print('I have %d apples.' %3)

print('rate is %s' %3.224)
print('rate is %f' %3.224)

# 문자열 포맷코드 %d를 % 기호랑 같이 쓰려면 % 기호를 %%로 써야한다
print('Error is %d%%' %98)
#print('Error is %d%' %98)

# %10s = 전체 길이가 10개인 문자열 공간에서 'HI'를 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 담겨두라
print('%10s' %'HI') # 8개 + HI
# '        HI'

# %-10s = 전체 길이가 10개인 문자열 공간에서 'HI'를 왼쪽으로 정렬하고 그 뒤의 나머지는 공백으로 담겨두라
print('%-10sjane' %'HI') # HI + 8개 + Jane
# 'HI        jane'

# %0.4f = 소수점 4자리까지 표시
print('%0.4f' %3.141529)

# %10.4f = 소수점 4자리까지 표시하되 전체 문자열 길이 10개에서 오른쪽 정렬
print('%10.4f' %3.141529) # 4개 + 3.1415(6개)
# '    3.1415'

#.format() 사용
print('I eat {0} apples.'.format(3))
print('I eat {0} apples.'.format('five'))
print('I ate {0} apples. So I was sick for {1} days.'.format(3, 'five')) # 입력 변수가 여러개이면 순서대로 {0}, {1}, {2}...
print('I ate {0} apples. So I was sick for {1} days.'.format(number3, day))
print('I ate {number} apples. So I was sick for {day} days.'.format(number = 3, day = 'five')) # 입력변수를 바로 {name} 처리
print('I ate {0} apples. So I was sick for {day} days.'.format(3, day = 'five'))

#.format() 정렬 사용
print('{0:<10}'.format('HI')) # :<10 -> HI를 왼쪽으로 정렬하고 총 문자열 10개
print('{0:>10}'.format('HI')) # :>10 -> HI를 오른쪽으로 정렬하고 총 문자열 10개
print('{0:^10}'.format('Hi')) # :^10 -> HI를 가운데 정렬하고 총 문자열 10개

#.format() 정렬하고 공백 채우기
print('{0:=^10}'.format('HI')) # :=^ -> HI를 가운데 정렬하고 총 10개 문자열의 나머지는 =로 채우기
print('{0:!<10}'.format('HI')) # :!< -> HI를 왼쪽 정렬하고 총 10개 문자열의 나머지는 !로 채우기

#.format()소수점 사용
y = 3.141529
print('{0:0.4f}'.format(y)) # print('%0.4f' %3.141529)
print('{0:10.4f}'.format(y)) # print('%10.4f' %3.141529)

print('{{ and }}'.format()) # .format() 사용해서 {} 문자열로 표현시
# { and }

# f접두사 = .format()
name = 'Kim'
age = 35
print(f'My name is {name}. {age} years old')
print(f'Next year, {age + 1} years old')

dic1 = dict(name = 'Kim', age = 30)
print(f'My name is {dic1["name"]}. {dic1["age"]} years old') # 딕셔너리 안에 있는 키값을 불러온다 {dic1["name"]}

print(f'{"HI":<10}')
print(f'{"HI":>10}')
print(f'{"HI":^10}')

print(f'{"HI":=^10}')
print(f'{"HI":!<10}')

print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{{ and }}')