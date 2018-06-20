a = 'Life is short, You need Python!'
print(a[0])
print(a[3])
print(a[-1])
print(a[-5])


print(a[0:4])
print(len(a[0:4]))
'''
첫 문자열 0
마지막 참조는 실제로는 -1
0 : 4 = 문자 0, 1, 2, 3
'''

print(a[0:5])    # 실제로는 life''
print(len(a[0:5])) # 문자 5개

print(a[5:13])

print(a[0:])
print(a[0:-8])  # 실제로는 -8-1 = -9니까 d

b = '20130331rainy'
date = b[:8]
year = b[:4]
month = b[4:6]
day = b[6:8]
print(date)
print(year)
print(month)
print(day)

weather = b[8:]
print(weather)

c = 'Pithon'
print(c[0] + 'y' + c[2:])
