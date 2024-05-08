from datetime import datetime
import time

now = datetime.now()

# strftime: str로 format하겠다. 특정한 형태로 출력할 예정이다
now.strftime("%Y-%m-%d %H:%M:%S")
for i in range(10):   
    print(now)
    time.sleep(1)   #1초마다 시간을 출력함, 1초씩 멈춘다
