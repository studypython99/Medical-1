#   1. 변수선언
score = [
    [80,90,85],[70,80,90],[84,92,80],[72,81,76]
]
name = ['홍길동','유관순','이순신','김구']
total = []

#   2. 코딩
#   2-1.    요소 하나하나 출력해보세요. 80, 90, 85, ...
for i in score:
    # print(i)
    for j in i:
        print(j,end=' ')
print()
#   2-2. 작은 요소의 합을 구해서 total에 넣어주세요.

for j in range(4):
    sum1 = 0    # @16번줄에 있으면 계속 더해진다 // sum1 이하의 조건이 수행된 값 1사이클
    # print(j)  j = 0,1,2,3
    for i in range(len(score[j])): # i = 0,1,2  
        # print(i)
        sum1 += score[j][i]
        '''
        1사이클: j=0, i=0,1,2 후, sum1
        2사이클: j=1, i=0,1,2 
        3사이클: j=2, i=0,1,2
        4사이클: j=3, i=0,1,2
        '''
    total.append(sum1)
print(total)
#           total = [a,b,c,d]
#   3. 출력
#   3-1. total = [225,240,256,229]
#   3-2. 250 미만 불합격, 250 이상 합격 ex) 홍길동님 합격입니다 출력
# name = ['홍길동','유관순','이순신','김구']
# total = [225,240,256,229]
for i in range(len(total)) :
    if 250 <= total[i] :
        print('{}님 {}점으로 합격입니다.'.format(name[i],total[i]))
    else:
        print('{}님 {}점으로 불합격입니다.'.format(name[i],total[i]))