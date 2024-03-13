#   1~100 사이 랜덤으로 숫자 1개 생성
#   입력한 숫자보다 크면 작은수를 입력하시오
#   입력한 숫자보다 작으면 큰 수를 입력하시오. 출력
#   정답을 맞추면 출력
#   총 입력한 횟수: n회 
#   입력한 숫자: n,n,n,n,n,n
import random
ran_num = random.randint(1,100)
ran_list = []
in_num = 0
cnt = 1
while True:
    in_num = int(input("{}회차, 숫자를 입력하세요 >>".format(cnt))) 
    ran_list.append(in_num)   
    if ran_num < in_num:
        print("{}보다 작아요.".format(in_num))
    elif ran_num > in_num:
        print("{}보다 큽니다.".format(in_num))
    elif ran_num == in_num:
        print("{}, 정답입니다.".format(in_num))
        break
    cnt += 1
for i in ran_list:
    print("총 입력한 횟수: {}회".format(cnt))
    print("현재까지 입력한 숫자: ",ran_list)
    break

'''
1. 홀 짝 = 50%
2. '''