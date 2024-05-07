import random
#   주택복권
#   글자 포함되어있다. str 으로 입력받아야한다.

#   조: 1~9
#   이후: 0~999999
#   랜덤으로 번호 설정 후 lotto에 입력
f_num = random.randint(1,9)
e_num = random.randint(0,999999)
#"{:06d}".format(30)


lotto = "1조111111" #str(f_num)+"조"+"{:06d}".format(e_num)

#   ex: 2조711 > 1개 번호가 맞았습니다.
l_input = "2조222211" #input("복권을 입력하세요. (ex:1조111) >>")
#   비교하는 프로그램을 구현하시오
#   자리수를 활용하세요
#   뒤에서부터 한자리씩 맞출때마다 상금
cnt = 0
for i in range(len(lotto),0,-1):
    if i ==2: continue #    조'는 건너뛰기
    if lotto[i-1] != l_input[i-1]:
        break
    else:
        cnt += 1    #   맞는 회수 1 증가
if cnt == 0:
    print("꽝")
elif cnt == 1:
    print("6번째 자리가 맞았습니다. 당첨금액: 1만원")
elif cnt == 2:
    print("5, 6번째 자리가 맞았습니다. 당첨금액: 10만원")
elif cnt == 3:
    print("4,5,6번째 자리가 맞았습니다. 당첨금액: 100만원")
elif cnt == 4:
    print("3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1000만원")
elif cnt == 5:
    print("2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 1억원")
elif cnt == 6:
    print("1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 10억원")
elif cnt == 6:
    print("1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액: 10억원")
