a_list = [1,2,3]

b_list = a_list
b_list[0] = 100

print(a_list)   #   얕은복사, 주소가 같다. >> [100, 2, 3]