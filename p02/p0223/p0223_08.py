#   점수를 입력받아서
#   1. 90점 이상: A / 80점 이상: B / 70점 이상: C / 나머지는 F
num = int(input('점수를 입력하세요 >>'))
# ABC의 범위를 설정
if num >= 90 :
    print('90점 이상입니다.')
    if num >= 98 :
        print('A+')
    elif num > 93 :
        print('A')
    else:
        print('A-')

elif num >= 80 :
    print('80점 이상입니다.')
    if num >= 88 :
        print('B+')
    elif num > 83 :
        print('B')
    else:
        print('B-')
elif num >= 70 :
    print('C')
else:
    print('F')
#   2. 98점 이상: A+ / 90~93: A- / 