# import datetime
from datetime import datetime   #now = datetime.datetime.now() 에서, now = datetime.now()    으로 datetime. 빼도 괜찮다
# now = datetime.now()
# from pytz import timezone
# print(datetime.now(timezone("asia/seoul")))

now = datetime.now()
print("시간을 포맷에 맞춰 출력")
#   Y:년 / m:월 / d:일 / H:시 / M:분 / S:초
output_a = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")    #   str format에 대한 time
output_a = now.strftime("%Y-%m-%d %H:%M:%S")    #   str format에 대한 time
output_a = now.strftime("%Y/%m/%d %H:%M:%S")    #   str format에 대한 time
print(output_a)

# print("현재시각 출력")              #   

# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")