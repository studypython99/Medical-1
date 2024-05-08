import random

class Card: #   클래스 선언, 파일관리, 보안, 코드의 재사용
    # kind = "" 아래에 사용되어서 없어도 괜찮다.
    # number = ""
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number

#   52장의 카드
#   spade, diamond, heart, clover
#   A,2,3,4,5,6,7,8,9,10,J,Q,K

#   랜덤 1장 뽑기
def random_one():
    num = random.randint(0,51)
    print("랜덤카드 1장:",num,card_list[num].kind,card_list[num].number)
    return card_list[num]
    
    

#   카드 생성
kind_list = ["spade","diamond","heart","clover"]
num_list = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
card_list = []
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],num_list[j]))
        
#   카드 출력        
for i in range(52):
    print("카드 ",card_list[i].kind,card_list[i].number)
    
#   랜덤으로 1장 뽑기
num = random.randint(0,51)
print("랜덤카드 1장:",num,card_list[num].kind,card_list[num].number)

#   랜덤 5장 뽑기 중복없이
#   1. 랜덤으로 줄 세워놓고 0,1,2,3,4, 가져오기
#       card_list shuffle
random.shuffle(card_list)
for i in range(5):
    print("5-1랜덤카드: ",card_list[i].kind,card_list[i].number)
print("-"*40)
#   2. 5장을 랜덤으로
#       card_list sample 5
ran_list = random.sample(card_list,5)
for i in ran_list:
    print("5-2랜덤카드: ",i.kind,i.number)
    
print("-"*40)

#   3. 1장 뽑고 기존 카드와 비교해서 다시 뽑기
temp_list = []
cnt = 0
while True:
    if cnt == 5 : break
    c = random_one()    #   랜덤카드 1장을 뽑아서
    for i in temp_list: #   리스트에 있는지 확인
        if c.kind == i.kind and c.number == i.number:
            continue
    temp_list.append(c)
    cnt += 1
for i in temp_list:
    print("5-3랜덤카드: ",i.kind,i.number)
    

    