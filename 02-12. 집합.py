s0 = set([1,2,3]) # set(1,2,3) 불가능
print(s0)
print(list(s0))

s1 = set(['hello']) #{'hello'}
print(s1)

s2 = set('hello') # {'o', 'e', 'h', 'l'}
print(s2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s1 = set([1,2,3])
s1.add(4) # 한개 원소만 추가
s1.add('up')
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6]) # 여러개의 원소 추가, 반드시 (['''']) 형태
s1.update(['up', 'down'])
print(s1)

s1 = set([1,2,3])
s1.remove(2)
print(s1)

#Q1
s0 =set(['a', 'b', 'c'])
print(s0)

#Q2
a1 = set([1,1,1,2,2,3,3,3,4,4,5])
print(a1)
a2 = set([1,1,1,2,2,3,3,3,4,4,5])
a3 = a1 & a2
print(a3)

a0 = list([1,1,1,2,2,3,3,3,4,4,5])
a1 = set(a0)     # 리스트 자료형이 집합 자료형으로 변환되면서 중복된 값들은 사라지게 된다
a2 = list(a1)
print(a2)

#Q3
s1 = set(['a','b','c','d','e'])
s2 = set(['c','d','e','f','g'])
s3 = s1 - s2
print(s3)

#Q4
a = set()
print(a)
print(type(a))

#Q5
a = set({'a','b','c'})
a.add('d')
a.add('e')
a.add('f')
print(a)

a = set({'a','b','c'})
a.update(['d','e','f'])
print(a)