print(200+100)
print(200-100)
print(200*100)
print(200/100)

#   quiz
#   1. 200 > 50으로 바꿔서 출력해보세요
#   2. 100 > 10
#   3. 10 > 30
#   4. 50 > 20
#   일일이 다 변경하기 귀찮... 그래서 변수 사용
#   변수를 사용 > 빠르고 쉽고 정확하게 할 수 있다.
a=100
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print('*'*20)
#   함수를 사용하여 사칙연산 계산
def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
cal(100,5)
print('-'*20)
cal(50,2)

num1=10
num2=5
print(str(num1)+'+'+str(num2)+'='+str(num1+num2))
print(num1,'+',num2,'=',num1+num2)
print('%d+%d=%d'%(num1,num2,num1+num2))
print('{}+{}={}'.format(num1,num2,num1+num2))

#   수식을 10-5=5로 출력하기 4가지방법 다 사용하기
num1=10
num2=5
print(str(num1)+'-'+str(num2)+'='+str(num1-num2))
print(num1,'-',num2,'=',num1-num2)
print('%d-%d=%d'%(num1,num2,num1-num2))
print('{}-{}={}'.format(num1,num2,num1-num2))