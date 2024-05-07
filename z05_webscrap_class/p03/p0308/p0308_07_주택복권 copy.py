import random
#   주택복권
#   글자 포함되어있다. str 으로 입력받아야한다.

#   조: 1~9
#   이후: 0~999999
#   랜덤으로 번호 설정 후 lotto에 입력
f_num = random.randint(1,9)
e_num = random.randint(0,999999)
#"{:06d}".format(30)


lotto = str(f_num)+"조"+"{:06d}".format(e_num)
print(lotto)
#   ex: 2조711 > 1개 번호가 맞았습니다.
l_input = input("복권을 입력하세요. (ex:1조111) >>")
#   비교하는 프로그램을 구현하시오
#   자리수를 활용하세요
cnt = 0
for i in range(len(lotto)):
    if lotto[i] == l_input[i]:  #   자리수가 같아서 i로 같이 사용해도 괜찮
        cnt += 1
print("{}자리 맞았습니다".format(cnt-1))
