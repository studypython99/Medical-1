class Card: #   4개의 번수: kind, number, width, height
    width = 0 #   클래스변수
    heigh = 0 #   클래스변수
    kind = ""
    number = ""
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200

    
# c1 = Card("spade","1")
# c2 = Card("spade","2")
# c3 = Card("spade","3")
# c4 = Card("shade","4")
# c5 = Card("shade","5")

card_list = []
for i in range(13):
    card_list.append(Card("spade",i+1))

for i in range(13):
    print(card_list[i].kind,card_list[i].number)
# card_list.append(Card("spade","A"))
# card_list.append(Card("spade","2"))
# card_list.append(Card("spade","3"))
# card_list.append(Card("shade","4"))
# card_list.append(Card("shade","5"))
# card_list.append(Card("shade","6"))
# card_list.append(Card("shade","7"))
# card_list.append(Card("shade","8"))
# card_list.append(Card("shade","9"))
# card_list.append(Card("shade","10"))
# card_list.append(Card("shade","J"))
# card_list.append(Card("shade","Q"))
# card_list.append(Card("shade","K"))

# print(len(card_list))   #   5
# print("리스트출력:",card_list[0].kind, card_list[0].number)


# #   52장 카드 생성
# shape = ["SPADE","DIAMOND","HEART","CLOVER"]
# number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# card_list = []
# for i in range(4):
#     for j in range(13):
#         c = Card(shape[i],number[j])  #   객체선언
#         card_list.append(c) #   리스트추가

# for i in range(52):
#     c = card_list[i]