# 공간을 만들어놓고 for문 사용
list = [0]*10
for i in range(10):
  list[i] = i+1
print(list)

# 컴프리헨션으로 방을 만들어놓고 데이터를 입력하는 방식이 빠름.
list1 = [i+1 for i in range(10)]
print(list1)

# 2차원 리스트: 크기가 지정이 안됨. 요소에 자료가 몇개 들어갈지 모름

a_list = []
a_list.append(0)  # 리스트에 append를 사용하여 추가. 단점: 느림.
a_list.append(1)
a_list.append(2)
print(a_list)

