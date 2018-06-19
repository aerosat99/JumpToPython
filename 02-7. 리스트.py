a = []
a = list()

a = [1, 2, 3, 4]
print(a[0] + a[2])    # 1+3
print(a[0] + a[-1])   # 1+4

b = [1, 2, 3, ['a', 'b', 'c']]
print(b[0])
print(b[-1])
print(b[3][0])
print(b[-1][1])

c = [1,2,3,4,5]
print(a[0:2])
print(c[2:4])
print(c[2:])

a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
d = a * 4
print(c)
print(c.count(3))
print(d)

# print(a[2] + 'hi')
print(str(a[2]) + 'hi')

a = [1, 2, 3]
a[2] = 4
print(a)

a = [1, 2, 3]
a[1:2] = ['a', 'b', 'c'] # a[1:2]
print(a)  # [1, 'a', 'b', 'c', 3]

a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print(a) # [1, ['a', 'b', 'c'], 3]

a = [1, 2, 3]
a[1:2] = ['a', 'b', 'c']
print(a)
a[1:3] = [ ]
print(a)
del a[1]
print(a)
