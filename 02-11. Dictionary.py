dic1 = {'name' : 'pay', 'phone' : '01099991111', 'birth' : '1118'}
print(dic1)
dic1 = dict(name = 'pay', phone = '01099991111', birth = '1118')
print(dic1)
print(dic1['name'])


a = {1 : 'a'}
a[2] = 'b'  #a[key] = value
print(a)
a['key'] = 'value'
print(a)
a[3] = [1, 2, 3, 4]   #Key에는 변하지 않는 값(튜플 가능, 리스트 불가능), value에는 변하는 값(리스트 가능)
print(a)
a[(4)] = (1 ,2, 3)

del a[1] #key 1, : value 'a'를 쌍으로 삭제
print(a)

dic1 = {'name' : 'pay', 'phone' : '01099991111', 'birth' : '1118'}
print(dic1.keys())
print(list(dic1.keys()))

print(dic1.values())
print(list(dic1.values()))

print(dic1.items())
print(list(dic1.items()))

dic1 = {'name' : 'pay', 'phone' : '01099991111', 'birth' : '1118'}
dic1.clear()  # clear()는 모든 요소 삭제, 개별 요소 삭제는 del dic['name']
print(dic1)

dic1 = {'name' : 'pay', 'phone' : '01099991111', 'birth' : '1118'}
print(dic1.get('name'))   # get(x) -> x에 해당하는 밸류 반환
print(dic1.get('phone'))
print(dic1['name'])
print(dic1.get('mail', 'nan')) # get(x, '디폴트값') -> x에 해당하는 키가 없을 때 미리 지정해놓은 디폴트값 반환

print('name' in dic1)

if 'name' in dic1 :
    print(True)
else :
    print(False)

#Q1
dic1 = dict(name = '홍길동', birth = 1128, age = 30)
print(dic1)
dic1 = {'name': '홍길동', 'birth': 1128, 'age': 30}

#Q2
a = dict()
a['name'] = 'python'  # 가능
a[('a', )] = 'python' # 가능, 키 값은 변하지 않는 항목 넣어야 하니 튜플 가능
a[250] = 'python'
print(a)
# a[[1]] = 'python'  # 불가능, 키 값에 변경 가능한 리스트 넣을 수 없다

#Q3
a = {'a':90, 'b' : 80, 'c':70}
print(a.keys())
print(a['b'])
print(a.get('b'))
del a['b']
print(a)

a = {'a':90, 'b' : 80, 'c':70}
a.pop('b')
print(a)

#Q4
a = {'a':90, 'b' : 80}
print(a.get('c', 70))

#Q5
a = {'A':90, 'B':80, 'C':70}
a1 = list(a.values())
a1.sort()
print(a1[0])

min(a.values())


#Q6
a = {'A':90, 'B':80, 'C':70}
print(list(a.items()))
