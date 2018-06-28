try :
    4 / 0
except ZeroDivisionError as e1 :
    print(e1)

try :
    f = open('minami.txt','r')
except FileNotFoundError as e2 :
    print(str(e2))
else :
    data = f.read()
    f.close()

try :
    f = open('foo.txt','r')
except :
    pass
finally :
    f.close()

# 먼저 발생하는 오류가 출력되고 두번째 오류는 출력되지 않는다
try :
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e1 :
    print(e1)
except IndexError as e2 :
    print(e2)

# 여러개의 오류를 한번에 처리
try :
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e1 :
    print(e1)

# 고의적 오류 발생
class Bird :
    def fly(self) :
        raise NotImplementedError  # 상속 받는 클래스에서 반드시 fly 매소드 구현해야 한다
#class Eagle(Bird) :
#    pass
#eagle = Eagle()
#eagle.fly()

class Eagle(Bird) :
    def fly(self):
        print('very fast')
eagle = Eagle()
eagle.fly()


# 예외 만들기
class MyError(Exception) : # 예외 클래스 만들기, 오류메시지를 내부 매소드로 구현
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def say_nick(nick) :
    if nick == '바보' :
        raise MyError('허용되지 않는 별명')
    print(nick)

try :
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
