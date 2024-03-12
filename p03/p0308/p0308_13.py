today_list = ['2024','03','08']
t_list = list(map(int,today_list))  # 리스트 내의 값을 int로 변환한 후 다시 저장해놓는다.
print(today_list)   #   ['2024', '03', '08']
print(t_list)       #   [2024, 3, 8]

#
int_list = [10,20,30,40,50]
str_list = list(map(str,int_list))  # int > str 로 변환
print(str_list) #   ['10', '20', '30', '40', '50']

a_list = list(map(str,range(10)))
print(a_list)   #   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#   input의 데이터 int변경해서 list저장
b_list = list(map(int,input("숫자입력: >>")))   #   333
print(b_list)  #   [3, 3, 3]