#   변수
a = False   #   bool
b = 123     #   정수
c = 1.345   #   실수
d = '문자'  #   문자열
e = [1,2,3] #   리스트

#   출력
print('안녕하세요')
print(123*456)
str1 = "반갑습니다"
print(str1) #   변수를 통한 출력
print('{0:s} : {1:d} / {2:d} = {3:f}'.format('수식',7,3,7/3))
print('{} : {} / {} = {}'.format('수식',7,3,7/3))   #   위 아래 같은 결과

#   관계연산자, 조건문이나 반복문에서 주로 사용한다.
#   > : 크다 >= : 크거나 같다. < : 작다 <= : 작거나 같다.
#   == : 같다 != : 같지 않다
print(3>5) #   결과가 거짓, False
n1 = 10
n2 = 8
print(n1 != n2) #   True

#   논리연산자: and or not
a, b = 10, 9
print('and연산자')
if a == 10 and b == 9 :
    print('참 and 참 = 참')
else:
    print('참 and 참 = 거짓')
    
if a == 10 and b != 9 :
    print('참 and 거짓 = 거짓')
else:
    print('참 and 참 = 참')
    
print('or연산자')   #   둘중 하나라도 참이면 참
if a == 10 or b != 9 :
    print('참 or 거짓 = 참')
    
print('not연산자')  #   참 > 거짓, 거짓 > 참
if not a == 10 :
    print('not 참 = 거짓')
else:
    print('not 참 = 참')
    
#   if
#   if 실행문1:
#       조건문1

num = 5
#   숫자가 0이상이면 양수를 출력하시오
if num >= 0:
    print('양수입니다.')
    
#   숫자가 0 이상이면 양수를 출력하고, 0미만이면 음수 출력
if num >= 0 :
    print('양수입니다')
elif num == 0 :
    print('0입니다.')
else:
    print('음수입니다.')    
    
#   실행문을 비우고 싶을 때 : pass
# if 조건문1:
#     실행문 대신에 pass
# else:
#     실행문
print('-'*20)    
if 1 == 1 :
    pass
else:
    print('else문 실행')
print('-'*20)    

#   중첩 if문: if문 안에 if문 사용
if num >= 0 :
    if num == 0 :
        print('0입니다')
    else:
        print('양수입니다')
else:
    print('음수입니다')
    

