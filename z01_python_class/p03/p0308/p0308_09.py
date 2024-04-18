import random
random_num = str(random.randint(10000,99999))
print("[랜덤숫자 맞추기]")
print("랜덤숫자:",random_num)
a_input = str(input("숫자 5자리를 입력하세요 >>"))
# random_num = "11111"
# a_input = "00001"
cnt = 0
for i in range(len(random_num)):
    if random_num[i] == a_input[i]:
        cnt += 1
print("{}자리 맞았습니다".format(cnt))
    
