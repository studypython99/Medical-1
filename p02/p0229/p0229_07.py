from random import *
#   랜덤숫자를 만들어서 (1~100)
#   내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램 종료.)
#   아니면 [다시 입력해주세요] 출력
#print(randint(1,100))   #   1~100 중에서 랜덤 숫자를 출력한다.
#   입력한 숫자가 랜덤숫자보다 작으면 큰 수를, 크면 작은 수를 입력하라고 이야기해주세요
#   1. 현재 입력한 숫자 모두를 inputList에 넣으세요.
#   2. 10회 도전 후 프로그램이 종료가 되게 해주세요.
inputList = []
rr = randint(1,100) #   while밖에서 딱 한번만 발생시킨다. 
i = 1
                    #   안에 있으면 계속 랜덤발생.
while i < 11:
    nn = int(input('내가 입력한 숫자 >>'))
    inputList.append(nn)
    print('{}회 남았습니다.'.format(10-i))
    i += 1
    print(inputList)
    if nn == rr:
        print('내가입력한:{}\n랜덤숫자는:{}\n당첨'.format(nn,rr))
        break
    elif nn > rr:
        print('작은 수를 입력해주세요.')
    elif nn < rr:
        print('큰 수를 입력해주세요.')
print(inputList)
print('10회 초과, 당첨번호는 {}입니다.'.format(rr)) #    rr 종료를 위해 보여준다?????????????????
                                        #   밖에서 한번 발생시킨 rr 값을 보여준다.
        