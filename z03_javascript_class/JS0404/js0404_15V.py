#12,1,2월 겨울 3,4,5월 봄 6,7,8월 여름 9,10,11월 가을

num = input("몇월?")
num1 = int(num[0:-1]) # 마지막 str 포함하지 않는다.

while 0<num1<13 :
    # if num1>12:
    #     print("다시 입력해주세요")
    if 2<num1<6:
        print(str(num1)+"월은 봄입니다.")
    elif 5<num1<9:
        print(str(num1)+"월은 여름입니다.")
    elif 9<num1<12:
        print(str(num1)+"월은 가을입니다.")
    elif num1==12 and num1<3:
        print(str(num1)+"월은 겨울입니다.")
    break
print("다시 입력하세요")