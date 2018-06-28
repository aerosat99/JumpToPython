#5-4-1
try :
    'a' + 1
except TypeError as e1 :
    print(e1)

print('a'+'1')

try :
    a = [1,2,3]
    a[3]
except IndexError as e2 :
    print(e2)

print(a[2])

#5-4-2
a = [1,2,3]
try :
    result = a[-3]
except :
    print('error')
else :
    print('No error')

#5-4-3
result = 3
try :
    result += 1
except :
    result += 2
else :
    result += 3
finally:
    result += 4

print(result)

#5-4-4
result = 0
try :
    [1,2,3][3]
    'a' + 1
    4 / 0
except TypeError :
    result += 1
except ZeroDivisionError :
    result += 2
except IndexError :
    result += 3
else :
    result += 4
finally:
    result += 5

print(result)



