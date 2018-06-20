t1 = (1, )
t2 = 1, 2, 3
t3 = ('a', 'b', ('ab', 'cd'))
# t2[1] = 4 -> error
# del t3[0] -> error

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

print(t1[1:])

t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)

#Q1
t1 = 3,
print(t1)

#Q2
t2 = (1, 2, 3)
t3 = (4, )
print(t2 + t3)
print(t2 + (4,))