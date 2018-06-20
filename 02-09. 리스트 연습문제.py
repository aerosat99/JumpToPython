#Q1
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
b = a[4] + ' ' + a[2]
print(b)

#Q2
a = ['Life', 'is', 'too', 'short' ]
b = ' '.join(a)
print(b)

#Q3
a = [1, 2, 3]
print(len(a))

#Q4
a = [1, 2, 3]
b = [4, 5]
a.append(b)     # print(a.append(b))로는 결과 안 나온다. 기존의 a 리스트가 이름은 그대로인채 요소만 바뀌는 것. print(a)로 호출해야 한다
print(a)        # [1, 2, 3, [4, 5]]

a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)        # [1, 2, 3, 4, 5]

#Q5
c = [1, 3, 5, 4, 2]
c.sort()
print(c)
c.reverse()
print(c)

#Q6
a = [1, 2, 3, 4, 5]
del a[1]    # [1, 3, 4, 5] 요소 위치(인덱스)를 입력
del a[2]    # [1, 3, 5]
print(a)

a = [1, 2, 3, 4, 5]
a.remove(2)    # [1, 3, 4, 5] 요소명을 직접 입력
a.remove(4)    # [1, 3, 5]
print(a)

a = [1, 2, 3, 4, 5]
a.pop(1)    # [1, 3, 4, 5] 요소 위치(인덱스)를 직접 입력
a.pop(2)    # [1, 3, 5]
print(a)