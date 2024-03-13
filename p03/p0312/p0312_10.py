import random

#   카드종류: SPADE, DIAMOND, HEART, CLOVER 총 4
#   카드숫자: A,2,3,4,5,6,7,8,9,10,J,Q,K  총 13
#   카드수량: 52장

def card_creat(shape_list,num_list,card_list,cnt):
    for i in shape_list:
        for j in num_list:
            card_list[cnt] = [i,j]            
            cnt += 1
              
def card_shuffle(card_list):
    random.shuffle(card_list)

def card_share():
    pass
def card_print():
    for i in range(5):
        print(card_list[i],end="")
#----------------------------------------------------------------------
card_list = [[0]*2 for i in range(52)]  #   [0]*2 = [0,0]
# print(card_list)
shape_list = ['spade','diamond','heart','clover']
num_list = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
cnt = 0 #   방마다 카드를 입력해주기위한 변수
for i in shape_list:
    for j in num_list:
        card_list[cnt] = [i,j]
        print(card_list[cnt],end='')    #   카드리스트 생성
        cnt += 1
    print()
print('-'*50)
random.shuffle(card_list)               #   카드리스트 랜덤
print(card_list)
print('-'*50)
for i in range(5):
    print(card_list[i],end="")          #   카드 5장 뽑기
print()
print('-'*50)



# while True:
#     print("[카드 프로그램]")
#     print("1. 카드생성")
#     print("2. 카드섞기")
#     print("3. 카드5장 나눠주기")
#     print("4. 카드5장 확인하기")
#     choice = int(input("원하는 번호를 입력하세요 >>"))

#     if choice == 1:
#         # card_creat()
#     elif choice == 2:
#         card_shuffle()
#     elif choice == 3:
#         card_share()
#     elif choice == 4:
#         card_print()
#     else:
#         print("프로그램을 종료합니다")
#         break