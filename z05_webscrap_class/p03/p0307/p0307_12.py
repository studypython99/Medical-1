list = [
      [0,0,0],[0,0,0],[0,0,0]
            
]
# 1차원 리스트에 1~9까지의 숫자를 입력하시오
list_1 = []
for i in range(9):
  list_1.append(i+1)
print(list_1)

# 2차원 리스트에 1~9까지의 숫자를 입력하시오  [[1,2,3],[4,5,6],[7,8,9]]
a_lists = []
for i in range(3):
  a_list = []
  for j in range(3):
    a_list.append((3*i)+j+1)
  a_lists.append(a_list)
print(a_lists)


# 컴프리헨션으로 작성    
list2 = [n+1 for n in range(9)] # n에 0~9까지를 n+1에 넣어서 list2에 저장해라
print(list2)

list3 = [[0]*3 for n in range(3)]
print(list3)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

numList = [num*num for num in range(1,6)]
print(numList)  # [1, 4, 9, 16, 25]

# list_2 = [["","",""],["","",""],["","",""]]
# for i in list_2:
#   for j in i:
    

