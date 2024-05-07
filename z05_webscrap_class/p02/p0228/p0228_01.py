#   변수 bool, int, float, string
a = False # bool은 참 or 거짓
b = 300 #   int 정수
c = 3.14    #   Float 실수
d = '문자열'    #   String 문자열

# #   input() >> 콘솔창에서 입력을 받는다
# e = input() #   input 문자열로 입력을 받는다.
# print(e)

'''
if 조건문1:
    실행문1
elif 조건문2:
    실행문2
else:
    실행문3
>> elif, else는 생략이 가능
if를 건너뛰고싶은 경우는 pass사용
ex) if 조건문:
        pass

'''
# n = int(input('숫자를 입력해주세요 >>'))
# if n >= 0 :
#     print('양수')
#     if n % 2 == 0 :
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('음수')

'''
반복문
for 변수 in 반복가능한데이터:
    실행문

'''
#   순차적으로 커질 때는 range를 사용한다
for i in range(0,3,1):  #   range(시작값, 끝값+1, 증감값)
    print('hi')         #   i가     0       2+1     1
    #   i = 0   일 때, hi
    #   i = 1   일 때, hi
    #   i = 2   일 때, hi
    
for i in range(5):  #   i를 0부터 4까지 반복해라 > 5회 반복
    print(1)    #   1을 5회 반복
    
for i in range(1,11):   
    print(i)    #   i를 11회 반복
    
print('-'*35)
a = 10
b = '안녕하세요'
#   a,b를 5번 반복해서 출력
for i in range(5):
    print(i)
    print(a)
    print(b)
    
#   입력: 이름, 점수, (5명의 이름과 점수를 입력)
#   60점 이상이면 합격, 미만이면 불합격 출력
#   출력의 형태는 '홍길동님 합격입니다.'or'홍길동님 불합격입니다'

for i in range(5):
    name = input('이름을 입력하세요 >>')
    score = int(input('점수를 입력하세요 >>'))
    if score >= 60 :
        print('{}님 합격입니다.'.format(name))
    else:
        print('{}님 불합격입니다.'.format(name))