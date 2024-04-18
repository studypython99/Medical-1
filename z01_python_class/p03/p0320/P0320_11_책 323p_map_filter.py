def jegob(val): #   map
    return val**2

def func(val):  #   filter
    return val >= 3

#   str을 int로 변경하고싶다
def int_change(val):
    return int(val)

a_list = [1,2,3,4,5]
str_list = ["1","2","3","4","5"]



#   리스트의 값이 하나씩 제곱에 부여된걸 리스트로 묶어서 제공한다
#   리스트 전체 값의 변경이 필요한 경우
map_list = list(map(jegob,a_list))
print(map_list)

#   a_list의 값을 함수 func에 하나씩 입력해서 결과를 리스트로 제공한다
#   특정값만 추출하는 경우
f_list = list(filter(func,a_list))
print(f_list)

ss_list = list(map(int_change,str_list))
print(ss_list)

#   람다식: 이름은 없애고 매개변수val을 사용해서 리턴값도 int(val)로 받아서 사용
ss_list2 = list(map(lambda val:int(val),str_list))
print("ss_list2: ",ss_list2)