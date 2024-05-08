#   함수선언
def cal(num1,num2):
    sum = 0
    temp = 0    #   java, javascript 에서 사용함
    if num1>num2:
        # num1,num2 = num2,num1   #   num1에 큰수가 들어온 경우
        temp = num1
        num1 = num2
        num2 = temp
    for i in range(num1,num2+1):
        sum += i

    return sum

#   두 수를 입력받아, 입력한 두 수 사이의 모든 합계를 구하는 프로그램
sum = 0
num1 = int(input("첫번째 숫자 >>"))
num2 = int(input("두번째 숫자 >>"))

# for i in range(num1,num2+1):      #   요 사이에 들어와야하는 함수선언
#     sum += i


sum = cal(num1,num2)

print("합계: ",sum)