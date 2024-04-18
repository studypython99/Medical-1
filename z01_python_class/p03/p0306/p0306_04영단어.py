import operator
import random
fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
         'grapes':'포도','mango':'망고','kiwi':'키위'}

#   복숭아를 영어로 입력하시오. 몇문제 맞췄는지 / 영어 단어장
right = 0
wrong = 0

for f in fruit:
    eng_in = input("{}를 영어로 입력하세요 >>".format(fruit[f]))
    #   비교하기: 입력값이랑 데이터랑 맞는지
    if eng_in == f:
        right += 1
        print("정답입니다.")
    else:
        wrong += 1
        print("틀렸습니다.")
    print("입력한 단어: {}".format(eng_in))
print(f'{right}개 맞았습니다.')
print(f'{wrong}개 틀렸습니다.')
#   총 갯수는 len(fruit)
