#   숫자 1개를 입력받아 출력하시오.

#   1. 숫자 1개 입력    #   1개와 n개 / 복사할 때 문제가 발생할 수 있다. 모두 리스트 쓴다고 좋은게 아님;

#   2. 숫자 1개 출력

# num = input('숫자를 입력하세요.')   #   str
# print(num)

# #   숫자 2개를 입력받아 출력하시오.
# #   1. 숫자 2개 입력
# num = int(input('숫자를 입력하세요.'))
# num1 = int(input('숫자를 입력하세요.'))
# print(num)
# print(num1)
# print(num+num1)

#   숫자 5개를 입력받아 출력하시오.
#   1. 숫자 5개 입력
#   2. 숫자 5개 출력
nums = []
for i in range(5):
    nums.append(int(input('숫자를 입력하세요 >>')))
    
print(nums)

#   5개의 합을 구하시오
sum = 0
for num in nums:
    sum += num
print(sum)
    