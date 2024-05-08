from random import *
#   1. 변수선언
lotto = []
mynum = []

#   1~10 사이의 숫자만 사용해서 로또 번호 생성하기
l = [1,2,3,4,5,6,7,8,9,10]
for i in range(50):
    temp = randint(0,9)         # l=[]의 0번방~9번방 까지 랜덤한 숫자 생성
    l[0],l[temp]=l[temp],l[0]
print(l)
for i in range(6):
    lotto.append(l[i])
print(lotto)
    