#   quizzzzzz
#   성별, 키를 입력받아서
#   남자일 경우 (M) 172.5 이상이면 [평균이상] 이하면 [평균이하]
#   여자일 경우 (F) 159.6 이상이면 [평균이상] 이하면 [평균이하]
#   그 외는 [잘못입력하셨습니다] 라고 출력해보세요
gender = input('성별을 입력하세요 (m/f) >>')
height = float(input('키를 입력하세요 >>'))

#   if, elif, else 를 거치면서 모든 경우의 수가 포함되어야한다.
if gender == 'm' or gender == 'M' :          #   만약에, 남자인데,
    print('남자')
    if height > 172.5 :     #   키가 172.5가 넘으면
        print('평균이상')    #  평균이상이야.
    else:
        print('평균이하')   #   안넘으면 평균이하야.
elif gender == 'f' :        #   만약에, 남자가 아니고 여자라면,
    print('여자')
    if height > 159.6 :     #   키가 159.6 이상이면
        print('평균이상')   #   평균이상이고,
    else:
        print('평균이하')   #   안넘으면 평균이하야.
else:
    print('잘못입력하셨습니다') #   만약에, 남자도 여자도 아니면 '잘못입력한거야'