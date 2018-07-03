# 메모장 생성
def make_memo(data) :
    with open('memo.txt','w') as f1 :
        f1.write(data)
        f1.write('\n')

# 조회
def read_memo(a) :
    with open('%s.txt'%a, 'r') as f2 :
        data = f2.read()
        print(data)

# 추가
def add_memo(data) :
    with open('memo.txt','a') as f3 :
        f3.write(data)
        f3.write('\n')

make_memo('2019')
read_memo('memo')
add_memo('Russia Worldcup')
read_memo('memo')
add_memo('Brazil')
read_memo('memo')