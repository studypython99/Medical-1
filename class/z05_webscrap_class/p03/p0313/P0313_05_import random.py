import random

print(random.random())                  #   0~0.99999999 랜덤으로 float의 결과값 리턴
print(random.uniform(10,20))            #   10~20사이 float
print(random.randrange(3))              #   =(0,3) 0~2까지 랜덤숫자 리턴 (3포함x)
print(random.choice([1,2,3,4,5]))       #   리스트 내 1개 랜덤 선택
print(random.sample([1,2,3,4,5],k=2))   #   리스트 내 k개 랜덤 선택
a_list = [1,2,3,4,5]
random.shuffle(a_list)                  #   a_list의 순서를 바꿔서 저장 (파괴함수)
print(a_list)
print(random.randint(1,10))             #   1~10(포함)범위의 int를 1개 선택
#-------------------------------------------------------------------------------------
from random import *             #   random 모듈명을 안붙여도 된다.
print(random())                  #   0~0.99999999 랜덤으로 float의 결과값 리턴
print(uniform(10,20))            #   10~20사이 float
print(randrange(3))              #   =(0,3) 0~2까지 랜덤숫자 리턴 (3포함x)
print(choice([1,2,3,4,5]))       #   리스트 내 1개 랜덤 선택
print(sample([1,2,3,4,5],k=2))   #   리스트 내 k개 랜덤 선택


# import math

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))