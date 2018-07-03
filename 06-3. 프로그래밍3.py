#
''' 게시판 페이징하기
    게시물의 총 건수(m) / 페이지당 보여줄 게시물 수(n) / 총 페이지수 구하기 '''

def getTotalPage(m, n) :
    if m % n != 0 :
        return round(m/n + 0.5, 0)    # 올림, 내림 함수가 별도로 없다면 올림은 반올림 + 0.5, 내림은 반올림 - 0.5
    else :
        return m/n

c1 = getTotalPage(5, 10)
c2 = getTotalPage(15, 10)
c3 = getTotalPage(25, 10)
c4 = getTotalPage(30, 10)

c0 = list()
c0.append(c1)
c0.append(c2)
c0.append(c3)
c0.append(c4)
print(c0)

def getTotalPage(m, n) :
    if m % n == 0 :
        return m // n
    else :
        return (m // n) + 1 # 나누기의 몫 + 1, // 나누기 후 소수점 아래 버린다

c5 = getTotalPage(5, 10)
c6 = getTotalPage(15, 10)
c7 = getTotalPage(25, 10)
c8 = getTotalPage(30, 10)

c9 = list()
c9.append(c5)
c9.append(c6)
c9.append(c7)
c9.append(c8)
print(c9)