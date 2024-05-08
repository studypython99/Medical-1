import random
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i # i-1자리에 1부터 13까지 입력
#print(num_list)    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
#print(num_list) ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

#   카드 1세트 완성하기 card_list 출력해보기
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list:    #모양 4가지
    for j in range(13): #숫자 13가지
        card_list[cnt] = [i,num_list[j]]    # 카드0번 = 모양0번,숫자0번 ...카드52번=모양4번,숫자13번
        print(card_list[cnt])
        cnt += 1

random.shuffle(card_list)
arr_num = 0
while True:
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")