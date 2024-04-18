#   1~100 까지 더하는데,
#   총 합이 100이 넘었을 때 수(i)를 출력하세요
#   ex) 1~10 까지 더하는데 총 합이 4가 넘는 수 출력
#       1+2+3 >>> 합이 10 > 4 따라서 3 출력
sum = 0
i = 0
i_list = []
while True:
    i += 1
    sum += i
    i_list.append(i)
    if sum > 100:
        print(i-1,'까지 더하면 100이 안넘어요.')
        break
print(i_list)
print(sum)