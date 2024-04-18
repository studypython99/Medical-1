#   quizzzz 
#   나이가 10살 이상이고 150 이상만 탑승가능
#   나이, 키를 입력받아
#   [탑승가능], [탑승불가능]을 출력해보세요

age = int(input('나이를 입력하세요 >>'))    #   input은 문자열로 입력받는다.
heigh = int(input('키를 입력하세요 >>'))

if age >= 10 :
    print('나이는 10살 이상입니다.')
    if heigh >= 150 :
        print('키는 150 이상입니다.')
        print('탑승가능')
    else:
        print('키 미달로 탑승 불가능')
else:
    print('나이제한으로 탑승 불가능')
    
#   숫자 3개 (정수)를 입력받고, 연산 1개(+-*/)를 입력받아
#   +++ --- *** /// (나누기 값은 둘째자리까지 표현)
#   a + b + c = d 의 형태로 출력 (1 + 2 + 3 = 6)

a = int(input('a값을 입력하세요 >>'))
b = int(input('b값을 입력하세요 >>'))
c = int(input('c값을 입력하세요 >>'))
dd = input('사칙연산 기호를 입력하세요 >>')
ee = a+b+c
ff = a-b-c
gg = a*b*c
hh = a/b/c
if dd == '+' :
    print('{}{}{}{}{}={}'.format(a,dd,b,dd,c,ee))
elif dd == '-' :
    print('{}{}{}{}{}={}'.format(a,dd,b,dd,c,ff))
elif dd == '*' :
    print('{}{}{}{}{}={}'.format(a,dd,b,dd,c,gg))
else:
    print('{}{}{}{}{}={:.2f}'.format(a,dd,b,dd,c,hh))
# print('{}{}{}{}{}={}'.format(a,dd,b,dd,c,ee))

if dd == '+' :
    ee = a+b+c
elif dd == '-' :
    ff = a-b-c
elif dd == '-' :
    gg = a*b*c
result = a #    result는 결과값
print('{}{}{}연산의 결과값은'.format(result)) # result로 결과값을 통일해서 받는다.