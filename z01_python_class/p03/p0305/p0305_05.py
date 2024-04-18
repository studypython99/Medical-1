#   1~25까지 숫자를 랜덤으로 섞은 후
#   2차원 리스트에 넣어보세요
import random

num = random.randint(1,100)   #   random 1,2,3

save_num = []
count = 0
#   숫자맞추기 프로그램 구현
#   1~10까지 숫자 랜덤으로 생성, 숫자를 맞추는 프로그램
while True:
    in_num = int(input('1~100까지의 숫자를 입력하세요 >>'))
    save_num.append(in_num)
    if num > in_num:
        print('입력한 숫자보다 더 큽니다.')
    elif num < in_num:
        print('입력한 숫자보다 더 작습니다.')
    else:
        print('{}번 만에 정답입니다.'.format(count))
        break   #   정답이 나올때까지 돌린다...
    count += 1      #   맨 위로 다시 돌아가려면 여기까지 와야한다.