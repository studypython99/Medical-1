'''
for 변수 in 반복가능데이터 :
    수행문장
    
for (변수)요소 in 리스트명 :
    반복하고싶은 실행문
for i in range(시작값, 끝값+1, 증감값) :
    반복하고싶은 실행문
>> 실행문이 i가 시작값부터 끝까지 반복

#   이중 for문장
for i in range(반복수1) :
    실행문1
    for j in range(반복수2) :
        실행문2
>> 실행문1이 반복수1 만큼 반복
>> 실행문2는 반복수1*반복수2 만큼 반복

'''
for i in range(5) : #   5회 반복 >> 0,1,2,3,4
    print('i= ',i)
    for j in range(3) : #   3회 반복 >> 0,1,2
        print('j= ',j)
        print('-'*25)
        
#   구구단
#   2단 출력
for i in range(1,10) :
    print('{}x{}={}'.format(2,i,2*i))
    
#   가로구구단 전체 출력
for i in range(2,10) :
    print('{}단'.format(i))
    for j in range(1,10) :
        print('{}x{}={}'.format(i,j,j*i),end=' ')
    print()
    
#   세로구구단
for j in range(2,10) :
    print('{}단'.format(j),end='\t')    
print()
for i in range(1,10) :
    for j in range(2,10) :
        print('{}x{}={}'.format(j,i,j*i),end='\t')
    print()