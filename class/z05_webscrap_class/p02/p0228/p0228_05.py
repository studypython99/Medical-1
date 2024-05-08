n1 = int(input('첫번째 숫자를 입력하세요 >>'))
n2 = int(input('두번째 숫자를 입력하세요 >>'))
sum = 0
#   n1~n2 까지의 합, 두 숫자를 비교해서  a > b 일 때 a,b = b,a 로 순서 변경해주기
if n1 > n2 :            #   비교는 밖에서 결정하고 들어오세요
    n1, n2 = n2, n1     #   한번만 결정되면 이하는 모두 적용된다.
for i in range(n1,n2+1):
    sum += i
print(sum)
odd_list = []
#   3. n1~n2 까지의 홀수 값을 저장
sum1 = 0
for j in range(n1,n2+1):
    if j % 2 == 1 :
        odd_list.append(j)
print(odd_list)
            

