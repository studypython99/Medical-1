#   quizzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
cal = input('수식을 입력하세요 (+,-,*,/) >>')
n1 = 24 # int
n2 = 5

#   수식 입력시 계산이 되도록, 수식 이외 입력시 +-*/중에 입력하시오. 출력

if cal == '+' :
    print(n1+n2)
elif cal == '-' :
    print(n1-n2)
elif cal == '*' :
    print(n1*n2)
elif cal == '/' :
    print(n1/n2)
else:
    print('+-*/ 중에 입력하세요.')

    