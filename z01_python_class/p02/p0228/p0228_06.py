from random import *

n1 = randrange(1,11)    #   1~10 까지의 랜덤한 정수
n2 = randint(1,10)      #   1~10 까지의 랜덤한 정수

#   랜덤한 숫자 6개 lotto리스트에 넣고
#   내가 입력한 숫자 6개는 mynum리스트에 넣어주세요

lotto = []
for i in range(6):
    n2 = randint(1,10)
    if n2 not in lotto:
        lotto.append(n2)

mynum = []
for i in range(6):
    nn = int(input('내가 입력한 숫자 >>'))
    mynum.append(nn)
    
print('lotto 숫자는:',lotto)
print('입력한 숫자는:',mynum)