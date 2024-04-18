def cal(n1,n2=10):  #   n2 = 10 키워드 매개변수는 제일 뒤에 와야함
    n1 = n1 + 10
    n2 = n2 + 20
    result = n1 +n2
    return  result
#---------------------------------------------------
num1 = 5
num2 = 7
result = cal(num1,) #   num1 >> n1 // n2??? 기본값 10을 쓰고, num2가 있으면 num2로 사용한다
cal ="현재숫자:,"(num1,num2,result)