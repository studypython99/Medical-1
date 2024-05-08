import datetime #   날짜관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴
print(now)

# #   시간을 사용해서 오전 오후 출력하기
# print(now.hour)
# time = now.hour
# if time<=12:
#     print('현재는',time,'시로 오전입니다.')
# else:
#     print('현재는',time,'시로 오후입니다.')

#   1. 짝수달 or 홀수달 입니다.
month=now.month
# if month%2 == 0:
#     print('지금은 {}월이며, 짝수달 입니다'.format(month))
# else:
#     print('지금은 {}월이며, 홀수달 입니다'.format(month))
print(month)
#   2. 겨울 or 다른계절
if 11<month or month<3:
    print('지금은 겨울입니다.')
else:
    print('겨울은 아닙니다.')
