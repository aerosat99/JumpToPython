# 문자 갯수 세기 .count()
a = 'hobby'
print(a.count(''))  # 6
print(a.count('b')) # 2

# 해당 문자 위치 .find()
b = 'Python is the best choice'
print(b.find('b')) # 14
print(b.find('k')) # -1 : 문자열에 포함되어 있지 않으면 -1 반환

# 해당 문자 위치 .index()
c = 'Life is too short'
print(c.index('t')) # 8
#print(c.index('k')) # Error : find 함수는 없으면 -1 반환, index 함수는 없으면 에러 메시지

# 문자 삽입 .join()
d = ','
print(d.join('abcd')) # a,b,c,d : 문자열 사이사이에 지정한 문자 삽입

# 소문자를 대문자로 .upper()
str1 = 'justice'
print(str1.upper()) # JUSTICE

# 대문자를 소문자로 .lower()
str2 = str1.upper() # JUSTICE
print(str2.lower()) # justice

# 왼쪽 공백 없에기 .lstrip()
e = '    hi'
print(e.lstrip()) # hi

# 오른쪽 공백 없애기 .rstrip()
f = 'hi    '
print(f.rstrip()) # hi

# 양쪽 공백 없애기 .strip()
h = '    hi    '
print(f.strip())

# 문자열 바꾸기 .replace(a, b) 'a'를 'b'로 바꾼다
print(c.replace('short', 'long')) # Life is too long

# 문자열 나누기 .split
print(c.split()) # 인수 없으면 공백을 기준으로 구분 ['Life', 'is', 'too', 'short']

i = 'a:b:c:d'
print(i.split(':')) # ''안의 구분자를 기준으로 구분 ['a', 'b', 'c', 'd']
