print("life" "is" "too" "short") #,없이 ""로 이어쓰면 +랑 같다
print("life"+"is"+"too"+"short")

print("life","is","too","short") # ,는 띄어쓰기 역할

# print는 기본적으로 결과를 줄바꿈 하는데, 줄바꿈 안할려면 맨 마지막에 end = ' '
for i in range(1,10) :
    print(i)

for i in range(1,10) :
    print(i, end = '')

for i in range(1,10) :
    print(i, ' ', end = '')

#Q1
input1 = int(input('First : '))
input2 = int(input('Second : '))

total = input1 + input2
print('Sum : %d'%total)

#Q2
list = input('입력 = ')
numbers = list.split(',')
sum = 0
for i in numbers :
    sum += int(i)
print(sum)

#Q4
def mul(a) :
    for i in range(1,10) :
        print(a * i, ' ', end = '')

a = int(input("2~9 : "))
mul(a)