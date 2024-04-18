#   quizzzz
#   1~100까지의 합을 구해보세요
sum = 0
for i in range(1,101):
    sum += i
print(sum)

#   1~100까지 짝수의 합을 구해보세요
sum1 = 0
for i in range(1,101):
    if i % 2 == 0 :
        sum1 += i
print(sum1)

#   1~100까지 홀수의 합을 구해보세요
sum1 = 0
for i in range(1,101):
    if i % 2 == 1 :
        sum1 += i
print(sum1)

#   위의 내용을 묶어서 표현 가능
s1,s2,s3 = 0,0,0
for i in range(1,101):
    s1 += i
    if i % 2 == 0:
        s2 += i
    else:
        s3 += i
print(s1,s2,s3)

#   1~10 합
#   리스트 안에 있는 값들의 합
m1 = 0
num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num)):
    m1 += num[i]
print(m1)

#   리스트 요소들을 불러오는 합
m2 = 0
for i in num:
    m2 += i
print(m2)