#   지역변수의 리스트와 전역변수의 리스트
#   전역변수 리스트를 매개변수로 전달시 리턴을 받지 않아도 된다.


# #   반환값이 여러개인 함수
# def multi(num1,num2):
#     result_list = []                #   지역변수는 이 밖을 벗어날 수 없다.
#     result_list.append(num1+num2)
#     result_list.append(num1-num2)
#     return result_list
    
# num1 = int(input("1숫자 입력 >>"))
# num2 = int(input("2숫자 입력 >>"))
# multi(num1,num2)
# print("결과값:",)    #   이렇게는 출력할 수 없다




#   반환값이 여러개인 함수
def multi(num1,num2):
    result_list.append(num1+num2)
    result_list.append(num1-num2)

    
result_list = []                #   전역변수는 이 밖을 벗어날 수 없다.
num1 = int(input("1숫자 입력 >>"))
num2 = int(input("2숫자 입력 >>"))
multi(num1,num2)
print("결과값:",result_list)    