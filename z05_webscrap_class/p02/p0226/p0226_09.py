numL = []

#   0에서부터 5까지 넣어보세요.
for i in range(6):
    numL.append(i)

print(numL)

aa = [1,2,3,4]
#   index를 사용해서 값 읽기
for i in aa :
    print(i)
    
for i in range(0,4):
    print(aa[i])
    
f = ['사과', '복숭아', '딸기', '포도', '자몽']
for i in f:
    print(i)
for i in range(len(f)): #   리스트의 길이 len 함수는 반복문에서 많이 사용
    print(f[i])
    
c = ['미국', '영국', '호주', '캐나도', '일본', '중국']
#   for문을 사용해서 출력해보기 2가지 방법
for i in c :
    print(i)
for i in range(len(c)):
    print(c[i],end=', ')
#   1에서 100까지 들어가는 numL=[]를 만들고 출력해보기
print() #   줄을 바꾸고 싶을 경우 사용
numL = []
for i in range(100):
    numL.append(i+1)    #   i 만 있으면 99까지 나옴.
    
print(numL,end=', ')
print()
for k in '안녕하세요':
    print('-',k,end=',')
    
#   반복문 안에 if문 사용(반대로도 사용 가능 if문 안에 반복문)
for i in range(10):
    print(i) #  0~9까지 출력
    if i == 9 :
        print('9입니다')
        
lan = ['영어', '스페인어', '일본어', '중국어']
for i in lan:
    print(i)
    if i == '영어':
        print('영어입니다.')
    else:
        print('다른언어입니다.')
        
#   2의 배수만 출력 (1~100)
#   1. 증감 사용
#   2. if 사용
for i in range(2,100,2):
    print(i,end=',')
print()
for i in range(100):
    if i%2 == 0 :
        print(i,end=' ')
        
#   7의 배수만 출력
for i in range(7,101,7):
    print(i,end=' ')
print()
for i in range(100):
    if (i+1)%7 == 0 :
        print(i+1,end=' ')
print()        

#   80점 이상만 합격 출력 > 합격이 5개 나온다.
aa = [100,90,86,79,72,52,98,94]
for i in aa:
    # print(i)
    if i >= 80 :
        print('합격')
        
f = ['사과', '복숭아', '딸기', '포도', '자몽']

#   딸기가 있으면 딸기, 다른과일은 다른과일 이라고 출력
for i in f :
    if i == '딸기' :
        print('딸기')
    else:
        print('다른과일',end=' ')
print()
num = [1,2,5,7,9,10,23,43]
#   짝수면 짝수, 홀수면 홀수 출력
#   1. for i in num:  >>> num 안의 요소로 접근
for i in num :
    if i % 2 == 0 :
        print(i,'짝수')
    else:
        print(i,'홀수')
        
#   2. for i in range(len(num)): >>> 숫자로 접근, n번째 요소로, index num[0] 0대신 i 입력
for i in range(len(num)):
    if num[i] % 2 == 0 :
        print(num[i],'짝수')
    else:
        print(num[i],'홀수')