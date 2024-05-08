class Lotto:
    number = 0
    shape = "circle"
    
    def __init__(self,number):
        self.number = number
        
#   lotto 1~45까지의 숫자를 입력한 리스트를 생성한 후 출력

lotto_list = []
for i in range(45):
    lotto_list.append(Lotto(i+1))

for i in range(45):
    print(lotto_list[i].number)