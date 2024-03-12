import random
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
# print(num_list) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
# print(num_list) ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
#   A>K>Q>j>10~2

#   카드 1세트 완성하기 card_list 출력해보기
card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list:    #   모양 4가지에
    for j in range(13): #   숫자 13가지
        card_list[cnt] = {"shape":i,"num":num_list[j]}   #   [모양,숫자]를 0~ 4x13=52 까지 입력한다
        print(card_list[cnt])
        cnt += 1
    
random.shuffle(card_list)
arr_num = 0
while True:
    print("1. 카드 1장 뽑기")
    print("2. 카드 5장 뽑기")
    print("0. 종료")
    c_num = int(input("번호를 선택하세요 >>"))
    if c_num == 1:
        print("모양:{}, 번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["num"]))
        arr_num += 1
    #   모양:spade, 번호:1 >>출력형태
    elif c_num == 2:
        for i in range(5):
            print("모양:{}, 번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["num"]))
            arr_num += 1
    elif c_num == 0:
        break