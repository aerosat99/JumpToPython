def sum(a, b) :  # a, b = 매개변수 parameter
    result = a + b
    return result

a = sum(3,4)   # 3, 4 = argument 인수
print(a)

def say() :    # 입력값이 없는 경우
    return 'HI'
a = say()
print(a)

def sum(a,b) :   # 결과값이 없는 경우
    print('%d와 %d의 합은 %d'%(a, b, a+b))
sum(3, 5)

def say() :      # 입력값, 결과값 모두 없는 경우
    print('HI')
say()

def sum(a, b) :  # a, b = 매개변수 parameter
    return a + b
a = sum(a = 1, b = 5)
print(a)

# parameter *args : 입력값들을 모두 모아서 튜플로 만들어준다, 여러개의 입력값을 일일이 함수 정의할 때 지정안해도 처리 가능
def sum_many(*args) :
    sum = 0
    for i in args :
        sum += i
    return sum

a = sum_many(1,2,3,4)
b = sum_many(7,9,10,4)
print(a)
print(b)

def sum_mul(choice, *args) :
    if choice == 'sum' :
        result = 0
        for i in args :
            result += i
    if choice == 'multi' :
        result = 1
        for i in args :
            result *= i
    return result

a = sum_mul('sum', 1,2,3,4)
print(a)
b = sum_mul('multi', 1,2,3,4)
print(b)

# **kwargs : 입력값을 key=value 형태로 주면 딕셔너리로 생성
def func(**kwargs) :
    print(kwargs)

func(a = 1)
func(name = 'foo', age = 30)

def func(*args, **kwargs) : # args 인수는 args튜플, kwargs 인수는 kwargs 딕셔너
    print(args)
    print(kwargs)
func(1,2,3,name = 'foo', age = 30)