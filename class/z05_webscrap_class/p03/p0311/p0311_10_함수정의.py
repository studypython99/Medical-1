#   함수선언 def 이름 ()    ex) def plus()
#   함수호출 이름 ()        ex) plus()
#   함수선언: def 이름(매개변수) >> 이름(매개변수)
#   리턴의 결과값을 받지 않아도 되지만, 리턴의 개수는 맞추야 한다.
#   함수 내의 변수는 지역변수여서, 함수가 종료되면 사라진다.
#   함수 내의 변경된 변수값을 전역변수에 반영하고 싶으면 return으로 돌려줘야함. 자주 쓰인다.
#   함수 내 global은 전역변수에 선언되어 있는 변수 주소를 가져온다. return이 없어도 된다. 자주 쓰이진 않는다. 데이터변경을 찾기가 힘들다.
#   매개변수로 list[], dict{}를 사용할 경우 return 할 필요가 없다.

#   함수선언
def func1(a,a_list):
    a = 100         #   지역변수
    a_list[0] = 100
    return a

a = 10              #   전역변수
a_list = [1,2,3]
#   함수호출
a = func1(a,a_list) #   2개 이상의 데이터를 저장하는 변수, 주소값을 저장한다 (list, dict 형태들)

#   데이터 출력
print(a)
print(a_list)










# def func1():
#     global a    #   전역변수를 가져옴. return이 필요없어진다.
#     a = 100      #   지역변수
#     print("func1 a =",a)
#     #   지역변수 값을 전역변수에 적용시키는 방법
#     #   코드를 추가하시오.
#     return a
# def func2():
#     print("func2 b =",a+10)
    

# a = 20          #   전역변수, 100으로 변경됨.
# a = func1()     #   100 따라서 100,
# func2()         #   110 (100에 10 더해준 값)
# print(a)


# def cal(v1,sum):    #   지역변수, 
#     sum = sum+500   #   함수 내에서만 사용 가능
#     v1 = v1+100
#     return v1, sum
# sum = 10         #   전역변수
# v1 = 100        #   전역변수
# cal(v1,sum)
# print(v1)       #   100
# print(sum)      #   10  함수 밖에서는 사용 불가

# sum, v1 = cal(v1,sum)
# print(v1)       #   510
# print(sum)      #   200  함수 밖에서는 사용 불가