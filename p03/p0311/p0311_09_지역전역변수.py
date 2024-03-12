def cal(input1,input2):
        r1 = input1+input2
        r2 = input1-input2
        r3 = input1*input2    
        r4 = input1/input2
        
        return r1, r2, r3, r4
    

input1 = int(input("첫번째 숫자를 입력하세요 >>"))
input2 = int(input("두번째 숫자를 입력하세요 >>"))
#   함수의 return을 사용해서 입력된 두 수의 사칙연산 결과값을 출력하세요.
#   20, 10
#   결과값: 30, 10, 200, 2
r1,r2,r3,r4 = cal(input1,input2)
data = cal(input1,input2)
print("결과값:",data)



# def plus(v1,v2):    #   이름은 같아도 다른변수이다.
#     v1 = v1+100
#     v2 = v2+200
#     return v1,v2    #   함수 밖에서 사용하려면 return 값을 돌려줘야 한다.
#                     #   여기에 쓰는것은 물론, 11번줄 처럼 받아줘야한다.
    
    
# #   함수호출
# v1 = 1
# v2 = 2
# v1, v2 = plus(v1,v2)    #   리턴으로 받아줘야 101, 202 으로 출력된다.

# #   출력
# print(v1,v2)