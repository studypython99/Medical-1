import random
# 1. 0으로 25개 1차원 리스트 생성
aList = [0]*25
# 2. 1로 5개를 변경
for i in range(5):
    aList[i] = 1
# 3. 랜덤섞기
random.shuffle(aList)
# 4. 5*5 2차원 리스트에 넣기
checkList = [[0]*5 for i in range(5)] #5*5의 공간을 생성
for i in range(5):
    for j in range(5):
       checkList[i][j] = aList[5*i+j]
#print("공간",aList)
#공간 [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# 추첨 5*5 2차원 배열
# print("체크리스트",checkList)
# 체크리스트 [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0]]
viewList = [["추첨"]*5 for i in range(5)] #5*5의 공간을 생성
r_count = 0
c_count = 0
while True:
    # 5. checkList 출력
    print("\t[ 5*5 checkList 좌표 ]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(checkList[i][j],end="\t")
        print()
    print("-"*40)
    # 6. viewList 출력
    print("\t[ 5*5 viewList 좌표 ]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(viewList[i][j],end="\t")
        print()
    print("-"*40)
    # 7. 좌표입력후 확인
    x = int(input("가로 좌표를 입력하세요.>> "))
    y = int(input("세로 좌표를 입력하세요.>> "))
    #   10회 시도 후 종료
    print("{}회 진행중입니다.".format(c_count))
    if c_count == 10:
        print("10회 종료.")    
        break
    elif checkList[x][y] == 1:
        viewList[x][y] = "당첨"
        c_count += 1
        print("{}회 당첨".format(r_count))
        if r_count == 5:
            print("5회 당첨으로 프로그램을 종료합니다.")
            break
    else:
        viewList[x][y] = "[꽝]"
        c_count += 1
        # 5개 다 맞으면 프로그램 종료
        
        
# card_list = [
#     {"shape":"spade","num":"A"},
#     {"shape":"spade","num":2},
#     {"shape":"spade","num":3},
#     {"shape":"spade","num":4},
#     ]
# card_list = [
#     ["spade","A"],
#     ["spade",2],
#     ["spade",3],
#     ["spade",4],
#     ]
card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
# 카드 1세트를 구현해서 출력하시오.
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list: # "spade","diamond","heart","clover"
    for j in range(13):
       card_list[cnt] = [i,num_list[j]]
       print(card_list[cnt])
       cnt += 1
# print(card_list)