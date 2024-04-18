from random import *

# n1 = randrange(1,10)    #   1~9 사이의 정수
# n2 = randrange(10)      #   0~10 사이의 정수
# n3 = randint(1,10)      #   1~10 사이의 정수

# print(n1,n2,n3)

lotto = []
#   lotto에 1~10 사이의 랜덤한 숫자 6개를 넣어보세요.

for i in range(100):
    n3 = randint(1,10) # 1~10 사이의 숫자를 랜덤으로 선택해라.
    if n3 not in lotto :  #   없으면 
        lotto.append(n3)    #   저장하세요 
    elif len(lotto) == 6 :    #   6개가 되었다면
        pass                        #   끝났습니다.
            
    

print(lotto)

mynum = []
# #   내가 직접 입력한 숫자 6개
# for i in range(6):
#     my = input('내 번호 입력 >>')
#     mynum.append(my)
# print(mynum)