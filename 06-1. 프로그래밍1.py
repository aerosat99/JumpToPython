#
''' 프로그램을 만들려면 가장 먼저 "입력"과 "출력"을 생각하라.
    숫자 / 문자, 단일(숫자) / 복수, 받는 형식은 주로 리스트 []    '''

def GuGu(a) :
    result = []
    for i in range(1,10) :
        result.append(i * a)
    return result

b = GuGu(2)
print(b)
print(type(b))