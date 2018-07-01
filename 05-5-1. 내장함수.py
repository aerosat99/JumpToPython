# abs
print(abs(-1.2))

# all
print(all([1,2,3]))
print(all([1,2,3,0])) # 하나라도 False 있으면 False 반환

# any
print(any([1,2,3,0])) # 모두 Falsed여야 False 반환
print(any([0,""]))

# chr : 아스키 코드를 입력하면 해당 문자를 반환 0~127
print(chr(97))
print(chr(34))

# ord : 문자를 아스키 코드로 변환
print(ord('a'))
print(ord('"'))

# dir : 객체가 자체적으로 가지고 있는 함수나 변수
print(dir([1,2,3]))
print(dir({'1':'a'}))

# divmod(a, b) : a를 b로 나눈 몫, 나머지
print(divmod(7, 3))

# enumerate : 반복되는 구문에서 객체의 위치를 알려주는 인덱스 값이 필요할 때
for i, name in enumerate(['baby','foo','bar']) :
    print(i, name)

# eval ' ' 안의 연산 가능한 문자열의 결과를 보여준다
print(eval('1+2'))
print(eval("'hi'+'a'"))

# filter(함수, 인수값) -> 참인 것만 걸러내서 보여준다
def positive(l) :
    result = []
    for i in l :
        if i > 0 :
            result.append(i)
    return result

print(positive([1, -3, 2, 0, 5, 6]))

def positive(x) :
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, 5, 6])))
print(list(filter(lambda x : x >0, [1, -3, 2, 0, 5, 6])))

# map(함수, 인수값) -> 결과 모두 보여준다
def two_times(numbers) :
    result = []             # 결과가 저장되는 변수는 리스트로 하자
    for i in numbers :
        result.append(i*2)
    return result

result = two_times([1,2,3,4]) # 여러개의 인수는 리스트로 입력하자
print(result)

def two_times(x) : return x * 2
print(list(map(two_times, [1,2,3,4])))
print(list(map(lambda a : a*2, [1,2,3,4])))

def plus_one(x) :
    return x+1
print(list(map(plus_one, [1,2,3,4])))
print(list(map(lambda x : x+1, [1,2,3,4])))

# min, max
print(min('python'))
print(max('python'))

# hex 16진수로 변환
print(hex(234))

# oct 8진수로 변환
print(oct(18))

# id
a = 3
b = a
print(id(3))
print(id(a))
print(id(b))

# int(x, Y) Y진수 x를 10진수로 변환해서
print(int('11', 2))
print(int('1A', 16))

# isinstance(인스턴스, 클래스) : 인스턴스가 그 클래스이면 True
class Person :
    pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))

# len : 문자열은 전체 개수
print(len('python')) # 1이 아니라 6

# list
print(list('python')) # ['p', 'y', 't', 'h', 'o', 'n']

# pow(x, y) -> x의 y 제곱 = x ** y
print(pow(2, 4))

# range(시작, 끝(-1), 간격)
print(list(range(5))) # 0,1,2,3,4
print(list(range(1,6))) # 1,2,3,4,5
print(list(range(2,19,4))) # 2,6,10,14,18

# round
from math import pi
print(round(pi, 2))
print(round(pi, 4))

# sorted (cf. 리스트 함수 .sort())
print(sorted([3,1,2]))   # 인수 여러개면 리스트로 입력
print(sorted(['a','v','g']))
print(sorted('zeros'))

a = [3,1,2]
a.sort()
print(a)

# str
print(str('hi'.upper()))
print(str('KIJH'.lower()))

# zip 동일한 갯수로 구성된 자료형을 순서별로 묶는다
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip('abc','def')))
