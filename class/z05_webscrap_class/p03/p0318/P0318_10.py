class Card:         #   사용자 정의변수, 그룹화 가능(kind,number...)
    kind = ""       #   클래스 카드의 종류
    number = ""     #   클래스 숫자의 종류, 데이터의 관리, 보안
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number

#   클래스를 이용해서 52장의 카드 생성

c_list = []
kind = ["spade","diamond","heart","clover"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c = Card(kind[i],number[j])
        c_list.append(c)

for i in range(52):
    print(c_list[i].kind,c_list[i].number)

#   리스트선언
# c_list = []
# kind = ["spade","diamond","heart","clover"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# for i in range(4):
#     for j in range(13):
#         c = [kind[i],number[j]]     #   리스트를 생성해서 리스트에 추가
#         c_list.append(c)
        
# print(c_list)        
#[['spade', 1], ['spade', 2], ...,['clover', 13]]

# for i in range(52):
#     print("카드:",kind[])







# c1 = Card("spade",1)    #   객체변수 선언   c1에 클래스의 kind와 number변수가 들어와있다

# #   c1에 숫자를 5로 변경하시오
# c1.number = 5

# #   c1을 출력하시오
# print(c1.kind,c1.number)    #   프린트를 변수로 하면 출력된다.

# #   c2 "heart", "A"
# c2 = Card("heart","A")
# print(c2.kind,c2.number)

# #   모양을 DIAMOND 변경 후 출력하시오
# c2.kind = "diamond"
# print(c2.kind,c2.number)
