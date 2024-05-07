# 공간을 같이 사용
list = [1,2,3]
alist = [*list] # 이런식으로 해야한다 ????????

list[0] = 100
print(alist)

# 공간을 따로 사용
a = 100
b = a
a = 10
print(b)  # a = 10, b = 100