#   숫자 두개를 입력받고,
#   연산자를 입력받아서 +-*/
#   무한히 계산하는 계산기를 만드는데
#   첫번째 숫자에 0을 입력하면 프로그램이 종료되는 코드


while True: #   무조건 참, break를 만나지 않는다면 무한반복
    n1 = int(input('첫번째 숫자 >>'))
    if n1 == 0 :                        #   첫번째 숫자에 0을 입력하면 아래 문구가 나온다
        print('계산기 종료되었습니다.') #   끝나기전에 마지막으로 할 말
        break                           #   끝!
    n2 = int(input('두번째 숫자 >>'))
    cc = input('연산기호를 입력하세요 >>')
    if cc == '+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif cc == '-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
    elif cc == '*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif cc == '/':
        print('{}/{}={}'.format(n1,n2,n1/n2))
    else:
        print('다시 입력하세요.')

    

# while True:                                     #   무한히 반복됨
#     n = input('숫자를 입력해주세요(종료: 0)')       
#     print(n)
#     if n == '0':
#         print('종료되었습니다.')
#         break
# print('프로그램이 종료되었습니다.')
