#   1. 0으로 25개 1차원 리스트 생성
alist = [0 for i in range(25)]
print(list)
    
#   2. 1로 5개를 변경
for i in range(5):
    alist[i] = 1
print(alist)
#   3. 랜덤 섞기
import random
random.shuffle(alist)
print(alist)

#   4. 5*5 2차원 리스트에 3. 입력
checklist = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checklist[i][j] = alist[5*i+j]
        
#   추첨 5*5 2차원 배열
viewlist = [["추첨"]*5 for i in range(5)]
answer_count = 0
c_count = 1
while True:
    #   5. checkList 출력
    for i in range(5)   :
        print(i,end='\t')
        for j in range(5):
            print(checklist[i][j],end='\t')
        print()
    print("-"*40)

    #   6. viewList 출력
    for i in range(5)   :
        print(i,end='\t')
        for j in range(5):
            print(viewlist[i][j],end='\t')
        print()
    print("-"*40)

############################################여기서부터 시작하기

    #   7. 좌표입력 후 확인
    x= int(input('가로 좌표 입력 >>'))
    y= int(input('세로 좌표 입력 >>'))
    if checklist[x][y] == 1:
        viewlist[x][y] = "당첨"

    #   내가 입력한 좌표 저장
    
    #   내가 입력한 좌표 print(my_xy)
    # 5개의 당첨을 맞추면 프로그램 종료
    # 10번 시도후 프로그램 종료
    # 현재까지 입력한 좌표를 모두 출력하시오.