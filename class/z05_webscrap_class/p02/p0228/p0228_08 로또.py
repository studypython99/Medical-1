#   1~45 사이의 숫자를 넣어서

#   1. 변수 선언
from random import *
mynum = [1,2,3,4,5,6]  #   입력을 1~45 사이의 숫자를 입력받음 (6개)
lotto = []  #   1~45 사이의 랜덤한 숫자 6자리 저장

#   2. 입력받은 숫자 6개
# for i in range(6):
#     n = int(input('{}번째 숫자를 입력하세요 (총 6개)>> '.format(i)))
#     mynum.append(n)
    
#   3. 로또 번호 생성하기

# 1~45 까지 번호 생성
l = []
for i in range(1,46):
    l.append(i)
#   중복없는 1~45
print('로또숫자(1~45): {}'.format(l))     

#   l = [1,2,3...........45]
#        0번방            44번방

for i in range(200):
    tmp = randint(0,44)     #   0~44번 사이 랜덤한 방번호 생성
    l[0],l[tmp]=l[tmp],l[0] #   200번 반복하면 순서가 대부분 바뀔것이다.
print('로또숫자(random 1~45): {}'.format(l))         

for i in range(6):          #   6번만 작동시켜서
    lotto.append(l[i])      #   0,1,2,3,4,5 번째 숫자만 l=[] 에 저장.
print('로또숫자 6개: {}'.format(lotto))         

# # 당첨확인, in / not in
ok = []
        
mynum1 = [1,2,3,4,5,6]  #   입력을 1~45 사이의 숫자를 입력받음 (6개)
lotto1 = [11,12,7,8,9,0]

for i in range(6):
    if mynum1[i] in lotto1 :
        ok.append(mynum1[i])
    elif mynum1[i] not in lotto1 :
        ok.append('꽝')
        
print('당첨된 숫자: {}'.format(ok))
