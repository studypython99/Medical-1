#   함수선언 def 이름() 정의
#   함수값은 return
#   함수호출 이름()
#   매개변수: 함수로 데이터전달하는 변수, 개수는 항상 같아야 한다.
#   가변매개변수선언: *values, 개수는 일치하지 않아도 된다.
#   리스트, 딕셔너리 매개변수는 주소값이 전달된다.

#   퀴즈1
#   함수를 사용하여 두 수를 입력받아, +-*/ 결과값을 출력하시오

def cal(num1,num2):
    result1 = num1+num2
    result2 = num1-num2
    result3 = num1*num2
    result4 = num1/num2
    
    return result1, result2, result3, result4

#   두 수 입력을 받아 값을 리턴받은 다음 출력하시오.
num1, num2 = 0,0

num1 = int(input("첫번째 숫자 >>"))
num2 = int(input("두번째 숫자 >>"))
result1, result2, result3, result4 = cal(num1,num2)
data = cal(num1,num2)

# print("{},{}결과값:".format(num1,num2)
print(result1, result2, result3, result4)   #   3 -1 2 0.5
print(data)                                 #   (3, -1, 2, 0.5) 변경x