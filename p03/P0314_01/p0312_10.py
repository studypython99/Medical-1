#   3월 13일 숙제입니다.!!

import random
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#   랜덤으로 2개를 뽑아서 출력
ran_num = (random.sample(c_number,k=2))
print(ran_num)
#   랜덤숫자 2 >> 1번방에 있습니다
#   랜덤숫자 9 >> 8번방에 있습니다
for i in ran_num:
    if i in c_number:
        print("랜덤숫자{} >> {}번방에 있습니다.".format(i,c_number[i]-2))
    print()
#   큰수: 9, 작은수: 2
if ran_num[0] > ran_num[1]:
    print("큰수: {}, 작은수: {}".format(*ran_num))
else:
    print("작은수: {}, 큰수: {}".format(*ran_num))
    
    '''
[5, 12]
랜덤숫자5 >> 4번방에 있습니다.
랜덤숫자12 >> 11번방에 있습니다.
작은수: 5, 큰수: 12
    '''