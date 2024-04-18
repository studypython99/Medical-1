import datetime

now = datetime.datetime.now() # 현재를 가져옴
print(now)

month = now.month

if 2 < month < 6 :
    print('봄')
    if month == 3 :
        print('이제 시작했습니다.')
    elif month == 4 :
        print('절정입니다.')
    else:
        print('곧 다음 계절이 옵니다.')
elif 5 < month < 9 :
    print('여름')
elif 8 < month < 12 :
    print('가을')
elif 0 < month < 3 or 11 < month < 13 :
    print('겨울')
else:
    print('그럴리가 없습니다.')