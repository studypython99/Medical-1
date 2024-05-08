#   산술 연산자
#   +-*/ 사칙연산
a=6
b=3
result=a+b
result=a-b
result=a*b
result=a/b
result=a//b #   //몫
result=a%b #   %나머지
result=a**b #   **제곱
print(result)

c=10
d=20
c,d=10,20

#   산술연산자 우선순위
#   곱셈, 나눗셈, 괄호가 우선순위. 나머지는 좌>우로 진행.

#   다른 자료형으로 연산
str1="문자열"
n1=10
print(str1*n1) #문자열문자열문자열문자열문자열문자열문자열문자열문자열문자열

#print(str1+n1) #errer

#문자열이나 정수, 실수의 경우 int(), float()를 사용하여 변환
s1="100"
s2="10.123"
print(int(s1)+1)
print(float(s2)+1)

#숫자가 아닌것은 변환할 수 없다.
# n=int("안녕하세요") # errer

#숫자를 문자로 바꾸고 싶으면 str()사용
n1=100
n2=10.123
print(str(n1),"1")
print(str(n2),"1")

p=12341234
print("010"+str(p))

#   숫자 두개를 입력받아서 나누기값, 몫, 나머지를 구하세요
#   ex) n1=4, n2=2
#   출력: 나누기값:(2.0) / 몫(2) / 나머지(0)

n1=int(input("첫번째숫자 >> "))
n2=int(input("두번째숫자 >> "))
print('나누기값:\t({})\n몫:\t\t({})\n나머지:\t\t({})'
      .format(n1/n2,n1//n2,n1%n2))