#   1~5까지의 합계를 구하세요.
sum = 1+2+3+4+5
print(sum)
total = 0           #   t = 0
total = total + 1   #   t = 1
total = total + 2   #   t = 1 + 2
total = total + 3   #   t = 1 + 2 + 3
total = total + 4   #   t = 1 + 2 + 3 + 4
total = total + 5   #   t = 1 + 2 + 3 + 4 + 5
print(total)

t = 0
for i in range(1,6,1) :
    t = t + i
print(t)

#   1~10까지의 합을 구하세요 for
sun10 = 0 # 변수의 초기화
for i in range(1,11) :
    sun10 += i
print(sun10)

#   1~100까지의 합
sum100 = 0
for i in range(1,101) :
    sum100 += i
print(sum100)

#   입력한 수부터 ~ 입력한 수 까지의 합을 구해보세요
#   n1, n2 를 입력받아서
n1 = int(input('첫번째 숫자를 입력하세요 >>'))
n2 = int(input('두번째 숫자를 입력하세요 >>'))

sum22 = 0
for i in range(n1,n2+1) :   # n1 은 시작하는 숫자, n2+1 은 n2까지
    sum22 += i
print(sum22)