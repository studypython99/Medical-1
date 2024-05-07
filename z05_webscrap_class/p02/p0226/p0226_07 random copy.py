# #   rnadom 함수
# from random import *

# print(random()) #   0.0 ~ 1.0 미만의 임의의 값 생성

# #   0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10))

# #   1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1)

# #   1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1)   #   1~46 미만의 임의의 값 생성
# print(int(random()*46))     #   1~46 미만의 임의의 값 생성
# print(randrange(1,46))      #   1~46 미만의 임의의 값 생성
# print(randint(1,45))    #   1~45 이하의 임의의 값 생성

# #   QUIZ
# #   1~10사이의 숫자를 입력받아서 변수1
# #   1~10사이의 랜덤한 숫자 변수2
# #   랜덤한 숫자와 비교해 같으면 [당첨]
# #   다르면 [랜덤숫자는 {}로 일치하지 않습니다.]

# num1 = int(input('1~10사이의 숫자를 입력하세요 >>'))
# num2 = randint(1,10)

# print('첫번째 숫자는',num1)
# print('두번째 숫자는',num2)
# if num1 == num2 :
#     print('당첨 입니다.')
# else:
#     print('랜덤숫자는 {}로 일치하지 않습니다.'.format(num2))

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers :
    output[0].append(number)

print(output)
