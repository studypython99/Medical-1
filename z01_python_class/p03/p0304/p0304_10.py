a = 10
b = a   #   변수 복사
b = 100     #   깊은 복사
print(a)    #   10
print(b)    #   100
a_list = [1,2,3]    
b_list = a_list     #   리스트 복사 / 얕은 복사
b_list[0] = 200     #   동일한 주소(방)을 사용한다. 
print(a_list[0])    #   200     
print(b_list[0])    #   200
