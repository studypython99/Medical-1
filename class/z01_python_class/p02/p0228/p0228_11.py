'''
주석 여러줄 쓸 때
한줄 주석 # 주석
ctrl + /
tab: 들여쓰기
shift + tab: 들여쓰기 삭제
alt + shift + 위 아래 방향키: 커서 있는 문장 복사
'''
num = [100,200,300,400]
#   for 문을 사용해서 하나씩 출력해보세요
#   2가지 방법이 있다. range in리스트명
for i in num:   #   num에 있는걸 그대로
    print(i)
    
for i in range(len(num)):   #   0,1,2,3... 요소요소의 번호를 가져온다
    print(num[i])

numlist = [[1,2],[3,4],[5,6]]
#   변수 in 리스트이름
for i in numlist:
    for j in i:
        print(j, end=' ')
    print()
    
#   in range
for i in range(len(numlist)):
    print(i)    #   i = 0,1,2
    for j in range(len(numlist[i])):
        print(numlist[i][j],end=' ')
    print()
    
f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]
#   요소 한개한개씩 출력해보세요
for i in f:
    #print(i)
    for j in i:
        print(j,end=', ')
    print()
    
for i in range(len(f)):
    #print(i)    #   0,1,2,3
    for j in range(len(f[i])):
        print(f[i][j],end=', ')
    print()
    
score = [90,80,70,100,95,85,100]
sum = 0
total = []
#   점수의 총 합을 구하세요
for i in score :
    #print(i)
    sum += i         # sum = sum + i   
total.append(sum)               #   들여쓰기를 더 생각해보자......
print(total)

sum1 = 0
for i in range(len(score)):
    sum1 += score[i]
print(sum1)