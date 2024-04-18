#     대입 연산자
#     =
a=3 # 3을 a에 넣는다.
a+=1 #      a=a+1
a=+2  #     a=a+2
#     +=, -=, *=, /=, //=, %=, **=
#     좌변, 우변에 동일한 변수명이 사용 될 경우 a=a+1
#     변수명을 생략하고 축약시킬 수 있다.

a=3
b=2
a*=2+b
#     a=a(2+b)    o
#     a=a*2+b     x

#     num이 20에서 시작해서 값이 누적됨
num=20
num+=2      #     num=num+2 = 22
print(num)
num-=2      #     num=num-2 = 20
print(num)
num*=2      #     num=num*2 = 40
print(num)
num/=2      #     num=num/2 = 20
print(num)
