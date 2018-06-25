# 함수의 결과값은 언제나 하나
def sum_mul(a,b) :
    return a+b, a*b

a = sum_mul(3,4)
print(a)          # a라는 변수에 7, 12 두개 들어있으나 함수의 결과값 a는 하나 (7, 12) 튜플 하나

n,m = sum_mul(3,4)
print(n)
print(m)

def say_nick(nick) :
    if nick == '바보' :
        return                 # return : 특정 조건에서 결과 없이 함수를 빠져나간다
    print('별명은 %s'%nick)

say_nick('JFk')
say_nick('Gate')
say_nick('바보')    # nick으로 '바보' 입력되면 아무것도 출력하지 않는다

# 매개변수에 미리 초기값 설정 : 초기값 설정하는 매개변수는 맨 마지막에 위치
def say_myself(name, age, man=True) :
    print('name : %s'%name)
    print('age : %d' %age)
    if man :
        print('Male')
    else :
        print('Female')

say_myself('Park', 30) # say_myself('Park', 30, 'Man')과 동일한 함수
say_myself('Park', 30, 'woman')

def say_myself(**kwargs) :
    name = kwargs['name']
    age = kwargs['age']
    print('name : %s'%name)
    print('age : %d' %age)

say_myself(name = 'Park', age = 30) # say_myself('Park', 30, 'Man')과 동일한 함수

# lambda
myList = [lambda a,b : a+b, lambda a,b : a*b]
print(myList[0](4,5))
print(myList[1](7,9))
print(myList)





