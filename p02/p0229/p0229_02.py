#   리스트변수명 = [요소1, 요소2,... ..., 요소n]
#   요소가 될 수 있는 타입: bool, in, float, string, list

fruits = ['딸기', '사과', '배', '수박', '귤']
#   귤을 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])

#   리스트에 요소를 추가
fruits.append('포도')
print(fruits)
fruits.remove('딸기')   #   특정요소를 삭제
print(fruits)

#   리스트에서 3번째 삭제
del(fruits[3])
print(fruits)

if '한라봉' in fruits :
    print('있다.')
    
for f in fruits :   #   in 리스트명
    print(f)
    
for i in range(len(fruits)) :   #   i = 0,1,2,3....
    print(fruits[i])
    
num = [[10,20,30],[100,200,300],[1,2,3]]
for n in num :  #   n = 0,1,2
    for a in n :
        print(a)
print('-'*25)
for i in range(len(num)):
    print(num[i])

for i in range(len(num)):
    print(num[i])
    for j in range(len(num[i])):
        print(num[i][j])
        
#   리스트에 숫자 넣을 때 한줄로 표현하기
aa = []
for i in range(1,11):
    aa.append(i)    #   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
print(aa)

a = [i for i in range(1,11)]    #   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 1~10까지 숫자를 채움
b = [0 for i in range(10)]    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 0을 10번 채움
b = [[0] for i in range(10)]    #   [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]] 
                                #   // [0]을 10번 채움
                                
print(a)
print(b)

a = [i*j for i in range(1,3) for j in range(1,3)]
#   [1,2,2,4,..........]

a = [i for i in range(100) if i%2 == 0]

b = [i for i in range(1,11)]    #   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 1~10까지 숫자를 채움
c = [i+1 for i in b]            #   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(c)

names = ['홍길동','유관순','이순신','강감찬','김구']
#   출력
#   1.홍길동 2.유관순 3.이순신 4.강감찬 5.김구
for i in range(len(names)):
    # print(i)
    print('{}.{}'.format(i+1,names[i]),end=' ')
    
#   변수1개 더 필요
i = 0
for name in names:
    i += 1
    print('{}.{}'.format(i,name))
    
#   enumerate 함수
#   index를 넣고 싶을 때 사용
for i , name in enumerate(names):   #   index : 0부터 시작
    print('{}.{}'.format(i+1,name))
    
#   start를 넣으면 시작을 조정
for i , name in enumerate(names, start=1):  #   index: 1부터 시작
    print('{}.{}'.format(i,name))
    
#   names = ['홍길동','유관순','이순신','강감찬','김구']
#               0       1       2       3       4

