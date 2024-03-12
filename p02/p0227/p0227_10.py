num = []
#   for문을 사용해서 1~10까지 숫자를 채우세요
for i in range(1,11):
    num.append(i)
print(num)

num1 = [i for i in range(1,11)]     #   한줄로 표현도 가능하다
print('한줄표현'+str(num1))

num2 = []
#   1~10까지 짝수를 num2리스트에 넣으세요
for j in range(1,11):
    if j % 2 == 0:
        num2.append(j)
print(num2)

#   num 리스트를 사용해서 1-10 까지의 합을 구하세요
num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for k in range(0,len(num)): #리스트의 순서 0,1,2,3, .... 를 사용한다.
    sum += num[k]
print(sum)

#   num 리스트 내 숫자들의 합을 구하세요
summ = 0
for i in num :  #   리스트 내 숫자들을 직접 가져온다.
    summ += i
print(summ)

#   num2 리스트 내 숫자들의 합을 구하세요
summm = 0
for i in num2 :
    summm += i
print(summm)