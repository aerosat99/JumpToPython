#5-2-1
a = all([1, 2, abs(-3)-3])
print(a)
# 마지막이 0(False)이기 때문에 False 반환

print(True) if chr(ord('a'))  == 'a' else print(False)
# True
# ord('a') = x(아스키코드) ,chr('x')  = a

print(ord('a'))
print(chr(97))

#5-2-2
d = dict()
for i, name in enumerate(['a','b','c']) :
    d[i] = name
print(d)

#5-2-3
c = list(filter(lambda x : x > 0, [1, -2, 3, -5, 8, -3]))
print(c)

#5-2-4
a = hex(234)
print(int(a,16))

#5-2-5
d = list(map(lambda x : x*3, [1,2,3,4]))
print(d)

#5-2-6
k = [-8,2,7,5,-3,5,0,1]
m = max(k)
n = min(k)
print(m,n)

j = sorted(k)
print(j)

k.sort(reverse=True)
print(k)

#5-2-7
print(round(17/3, 4))

#5-2-8
v = list(zip([1,2,3,4], ['a','b','c','d']))
print(v)