import random

w_list = ["토마토","바나나","사과","배","수박","메론","복숭아"]

#   random.random()
print(random.random())  #   0~1사이의 실수생성 0 < 0.789462075718218 < 1

#   정수형 랜덤숫자 생성(시작,끝)
print(random.randint(1,3))      #   1,2,3

#   시작,끝-1 // 생성
print(random.randrange(1,3))    #   1,2

#   리스트를 랜덤으로 섞기
list = [1,2,3,4,5,6,7]
print(list)
random.shuffle(list)
print(list)

#   리스트에서 1개를 랜덤으로 추출
print(random.choice(list))

#   리스트에서 해당되는 개수만큼 랜덤으로 추출(중복안되는 상태에서 2개 가져온다)
print(random.sample(list,2))
w_list = ["토마토","바나나","사과","배","수박","메론","복숭아"]
print(random.sample(w_list,3))

