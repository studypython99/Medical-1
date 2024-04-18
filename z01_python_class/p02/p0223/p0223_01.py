#   출력 print()
print('문자열') #   문자열 출력
print(10.123)   #   숫자출력
print(123*111)  #   사칙연산 후 출력

#   %d 정수 / %f 실수 / %s 문자열
print("%d %f %s"%(10,1.1,'문자'))
print("%.2f"%(23.232124))   #   소숫점 둘째자리까지 출력

#   str.format()
print('문자열을 쓰고 {}.'.format(1))

#   정수
print("{0:d}".format(123))  # 0, 첫번째칸부터 / d, 정수로 출력할거야
print('{0}'.format(123))
print('{}'.format(123)) #   123 모두 같은값 출력

#   실수
print('{0:f}'.format(123.456789))   #   format() <- 이 괄호 안의 내용을 0부터 시작
print('{0}'.format(123.456789))
print('{}'.format(123.456789))

#   문자
print('{0:s}'.format('문자'))
print('{0}'.format('문자'))
print('{}'.format('문자'))

#   변수
number = 10         #   정수
pi = 3.14           #   실수
result = True       #   bool True, Fales
str1 = '문장입니다.' #   string
ch = 'a'            #   문자

s1 = '1+1=2'
print(s1)
s2 = '{}+{}={}'.format(1,1,2)
print(s2)

a = 1
a = a + 1
a += 1      #   =+, -=, *=, /=, //=, %=

a,b = 10,20 #   한줄로 표기 가능

print(a == b)   #   T, F 판별
print(a != b)   #   ! > not
print(a > b)
print(a >=b)

#   논리연산자: and, or, not.
a,b,c = 100,200,150
result = (a > c) and (b < c)
print(result)

r1 = True
print(not r1)   #   False

#   입력받기 input()
name = input("이름")
print('내 이름은 {}입니다.'.format(name))
#   input()의 결과값은 문자형
age=int(input('나이를 입력하시오'))     #   문자를 정수형으로 바꿔주는 int()
print('당신은 올해 {}살 입니다.'.format(age+1))

#   if 조건문
#   if 조건문1:
#       실행문1
#   [else:
#       실행문2]
#   조건문1 참이면 실행문1 실행 후 종료
#   조건문1 거짓이면, 실행문2 실행 후 종료
f='apple'
if f =='banana':
    print("맞아요")
else:
    print("달라요")