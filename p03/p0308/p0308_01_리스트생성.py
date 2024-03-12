#   리스트
list = []
#   1~10까지 입력해보세요
for i in range(10): #   1. append사용
    list.append(i+1)
print(list)

list1 = [ i+1 for i in range(10)]   #   2. 컴프리헨션
print(list1)

list2 = [""]*10       #   3. 공간을 만든 후
for i in range(10):
    list2[i] = i+1  #   입력한다
print(list2)