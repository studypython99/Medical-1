import time
import random
#   웹 스크래핑 시, 차단을 피하기 위한 랜덤대기
for i in range(100):
    if i % 10 == 0:     #   10의 배수가 나오면 ex) 10,20,30, ... ,90, 100
        # time.sleep(3)   #   3초 자라
        num = random.randint(1,3)
        print(num,"초 대기")
        time.sleep(num)
        
        pass
    print(i)