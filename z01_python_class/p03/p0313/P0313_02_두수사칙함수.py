#   함수선언 def 이름() 정의
#   함수값은 return
#   함수호출 이름()
#   매개변수: 함수로 데이터전달하는 변수, 개수는 항상 같아야 한다.
#   가변매개변수선언: *values, 개수는 일치하지 않아도 된다.
#   리스트, 딕셔너리 매개변수는 주소값이 전달된다.

#   퀴즈1
#   함수를 사용하여 두 수를 입력받아, +-*/ 결과값을 출력하시오

def cal(num1,num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1+num2
    r_list[3] = num1-num2
    r_list[4] = num1*num2
    r_list[5] = num1/num2
    
    return r_list
#   두 수 입력을 받아 값을 리턴받은 다음 출력하시오.
save_list = []
while True:
    num1 = int(input("첫번째 숫자 (0.종료)>>"))
    if num1 == 0:
        break
    num2 = int(input("두번째 숫자 >>"))
    r_list = cal(num1,num2)
    #   save_list에 r_list를 저장

    # print("{},{}결과값:".format(num1,num2)
    print("{},{} 결과값: {},{},{},{:.2f}".format(*r_list))
    save_list.append(r_list)
    
#   현재까지 입력한 모든 값을 출력
for s in save_list:
    print("{},{} 결과값: {},{},{},{:.2f}".format(*s))
    

