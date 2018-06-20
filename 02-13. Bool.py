# 비어있는 리스트, 튜플, 딕셔너리는 거짓, 0은 거짓
if {} :
    print(True)
else :
    print(False)

print(bool('OP'))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))

a = list([1,2,3,4])
while a :
    print(a.pop())
    print(a)
# 빈 리스트가 되어 거짓이 되면 while 중단

#Q1
print(1 != 1)
print('a' in 'abc')
print('a' not in [1, 2, 3])

#Q2
a = 'python'
b = " " # 스페이스 한칸(공백 하나) 있기 때문에 True
c = ""
d = (1,2,3)
e = 0
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))