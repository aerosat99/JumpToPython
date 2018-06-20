a = list(range(1,4))
print(a)

#.append(v) 원래 리스트 마지막에 v 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#.sort()
a = [1, 4, 3, 2]
a.sort()
print(a)
a.sort(reverse=True) # 기본 옵션이 reverse=False
print(a)

#.reverse() 순서를 반대로, 정렬은 안해준다
a = [1, 4, 3, 2]
a.reverse()
print(a)

#.index()
a = ['b', 'x', 'r', 'y']
b = a.index('y')
print(b)

#.insert(a,b) 리스트 a번째 위치에 b 삽입, 기존 요소는 뒤로 밀린다
a = [1, 4, 3, 2]
a.insert(0,1)
print(a)
a.insert(4,7)
print(a)

#.remove(x) 리스트에서 첫번째로 나오는 x를 삭제
a = [1, 2, 3, 1, 2 ,3]
a.remove(1)
print(a)
a.remove(3)
print(a)

#.pop() 가장 마지막 요소를 반환하고 그 요소를 삭제
#.pop(x) x번째 요소를 반환하고 그 요소를 삭제
a = [1, 2, 3, 1, 2 ,3]
a.pop()
print(a)
a.pop(1)
print(a)

#.count(x) 리스트 안에 x 몇개 있는지
a = [1, 2, 3, 1, 2 ,3]
b = a.count(2)
print(b)

#.extend(x) 기존 리스트에 새로운 리스트 x를 더한다
a = [1,2,3]
a.extend([4,5,6])
print(a)
b = [7,8,9]
a.extend(b)
print(a)

# remove(), pop(), del
a = [1, 2, 3, 'a', 'b', 'c']
a.remove('a')   # 요소 'a'를 삭제
print(a)

a = [1, 2, 3, 'a', 'b', 'c']
a.pop(3)   # 4번째 요소('a')를 삭제
print(a)

a = [1, 2, 3, 'a', 'b', 'c']
del a[3]   # 4번째 요소('a')를 삭제
print(a)
