#Q1
def is_odd(a) :
    if a % 2 == 0 :
        print('Even')
    else :
        print('Odd')

is_odd(3)
is_odd(8)

#Q2
def average(*args) :
    sum = 0
    for i in args :
        sum += i
    return sum/int(len(args))

a = average(1,3,5)
b = average(178,848,546,952)
print(a)
print(b)

#Q3
def mul(a) :
    for i in range(1,10) :
        print(a * i)

a = int(input("2~9 : "))
mul(a)

#Q4
def fib(a) :
    if a == 0 :
        return 0
    if a == 1 :
        return 1
    return fib(a-2) + fib(a-1)

for a in range(1, 10) :
    print(fib(a))

#Q5
def myfunc(numbers):
    result = []
    for number in numbers:
        if number > 5:
            result.append(number)
    return result

print(myfunc([2,3,4,5,6,7,8]))

myfunc = lambda numbers:[number for number in numbers if number > 5]
print(myfunc([2,3,4,5,6,7,8]))
