'''
반복문 - for, while
for 변수 in 반복가능한데이터:
    수행문
    
for 카운터변수(i) in range(시작값, 끝값+1, 증감값)
    수행문(들여쓰기 필수)
'''
for i in range(0,10,1):     #(0,10,1) 0부터 9까지 1씩 증가한다. 0~9
    print('수행문입니다.')

for i in range(0,10,2):     #(0,10,2) 0부터 9까지 1씩 증가한다. 0,2,4,6,8
    print('수행문입니다.')

for i in range(0,3):        #(0,3)  0부터 3까지 1씩(안쓰면 1로 고정)
    print('두번째 수행문')
    
for i in range(5):          #   5번 반복하자
    print('세번째 수행문입니다.')
    
print('-'*35)
for i in range(3):          #   3번 반복 (0부터 생략, 1씩증가 생략(0,3,1))
    print(i)
    
#   카운터변수i를 사용하지 않을 때 _로 사용이 가능하다
for _ in range(5):          #   5번 반복하자
    print('세번째 수행문입니다.')
    
for i in range(10,0,-2):    #   10에서부터 0까지 -2씩 감소
    print(i,'증감 2: 수행문')   

l1 = [100,200,300,400,500]
#   리스트 안 요소 확인 in / not in
'''
for 변수 in 리스트명:
    실행문
    
for 변수 in range(len(리스트명))
    실행문
    리스트명[변수]    
'''
for n in l1:
    print(n)
    
for i in range(len(l1)):    #   l1 리스트의 요소 갯수를 i 라고 해보자 0~n(l1 갯수만큼)
    print(i)    #   0,1,2,3,4, ... 
    print(l1[i])    #   l1[0], l1[1], li[2], ...  그 갯수를 [] 안에 입력.
    
#   quiz
#   1. for문을 사용해서 1-100 사이의 홀수를 출력해보세요
#   1-1     if 사용하지 않음, 증감이용
for i in range(1,100,2):
    print(i,end=',')
print()
#   1-2     if 사용
for i in range(100):        #   1~100까지 출력한다
    if i%2 == 1:            #   2로 나누었을 때 %나머지가 1이라면
        print(i,end=',')    #   출력한다
    else:
        pass
print()
#   50~1 사이의 6의 배수를 역순으로 출력
for i in range(48,1,-6):
    print(i,end=',')
print()    

#   quiz
#   input()사용해서
#   입력: 두개의 숫자를 입력받는다
#   출력: 사칙연산
            # a + b = c
            # a - b = d
            # a * b = e
            # a / b = f
#   계산을 10번 반복하는 코드를 만드세요
# for i in range(10):      #   10번 반복
#     n1 = int(input('첫번째 숫자를 입력하세요 >>'))
#     n2 = int(input('두번째 숫자를 입력하세요 >>'))
#     print('{}+{}={}'.format(n1,n2,n1+n2))
#     print('{}-{}={}'.format(n1,n2,n1-n2))
#     print('{}*{}={}'.format(n1,n2,n1*n2))
#     print('{}/{}={:.2f}'.format(n1,n2,float(n1/n2)))
#     print(i+1,'번 실행했습니다.')
    
#   연산자를 입력받아서 if 문을 사용하여 출력.
for i in range(10):      #   10번 반복
    n1 = int(input('첫번째 숫자를 입력하세요 >>'))
    n2 = int(input('두번째 숫자를 입력하세요 >>'))
    co = input('연산기호를 입력하세요(+,-,*,/) >>')
    if co == '+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
        print(i+1,'번 실행했습니다.')
    elif co == '-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
        print(i+1,'번 실행했습니다.')
    elif co == '*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
        print(i+1,'번 실행했습니다.')
    elif co == '/':
        print('{}/{}={:.2f}'.format(n1,n2,float(n1/n2)))
        print(i+1,'번 실행했습니다.')
    else:
        pass