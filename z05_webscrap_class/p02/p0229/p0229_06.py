#   continue 예제
#   1~100 합계를 구하는데, 3의 배수는 제외하고 더하기
#   1~100 까지 출력 (단, 3의 배수 제외)
i = 0
sum = 0
while i < 100:
    i += 1
    # print(i)
    if i % 3 == 0:
        continue
    sum += i
    # print(i,end=', ')
print(sum)