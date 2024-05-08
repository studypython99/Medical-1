
for j in range(5):       # 이중 for문 사용시 ijklmn 각기 다르게 사용하세요
    gugudan = int(input('구구단 몇단을 보여드릴까요 >>'))
    print('-'*3+'구구단'+str(gugudan)+'-'*3)
    for i in range(1,10):
        print('{}x{}={}'.format(gugudan,i,gugudan*i))