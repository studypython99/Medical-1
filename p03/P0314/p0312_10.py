import random

c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
    
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]


#   랜덤으로 2개를 뽑아서 출력
print(random.sample(c_number,k=2))

#   랜덤숫자 2 >> 1번방에 있습니다
#   랜덤숫자 9 >> 8번방에 있습니다
#   큰수: 9, 작은수: 2


