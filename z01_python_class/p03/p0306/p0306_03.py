import operator
#   numbers에 있는 숫자들이 몇번 나왔는지
#   딕셔너리로 출력하시오.
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}
for i in numbers:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1
print(counter)  #   {1: 5, 2: 1, 4: 4, 6: 2, 3: 3, 7: 6}

array = ["F","D","A","C","A","C","F","B","C","E"]
counter1 = {}
for i in array:
    if i not in counter1:
        counter1[i] = 0
    counter1[i] += 1
print(counter1)     #   {'F': 2, 'D': 1, 'A': 2, 'C': 3, 'B': 1, 'E': 1}
print(sorted(counter1.items(),key=operator.itemgetter(0)))  #   key 정배열  [('A', 2), ('B', 1), ('C', 3), ('D', 1), ('E', 1), ('F', 2)]

t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
         'grapes':'포도','mango':'망고','kiwi':'키위'}