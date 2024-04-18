#   list
#   데이터를 잘 관리하기 위해서 묶어서 관리하는 자료형
#   리스트변수명 = [요소1, 요소2, 요소3..............]
list1 = []
list2 = [0,3,5]
list3 = ['짝수','홀수']
list4 = ['홍길동', 100, 20.003]
list5 = ['짝수', [2,4,6], '홀수']
#   list자체도 하나의 요소로 사용 가능

#   인덱싱(index) 리스트를 검색, 접근
#   index는 0 부터 시작
numL = [0,1,2,3,4]
#   0을 출력
print(numL[0])  #   두 값이 동일
print(numL[-5])

#   인덱스를 가지고 리스트의 특정 요소 값을 수정할 수 있다.
#   리스트[n] = 값
numL[0] = 20    #   [0] 위치의 값을 20으로 바꿀것이다.
numL[-1] = 222
print(numL)

#   list5 = ['짝수', [2,4,6], '홀수']
#   숫자 2에 접근하기 위한 방법
print(list5[1][0])

#   리스트 슬라이싱: 리스트 자르기
#   콜론: 을 사용해서 ~부터 ~까지
#   리스트명[시작인덱스 : 끝인덱스+1] 시작은 포함, 끝자리는 제외
#   numL = [0,1,2,3,4]
print(numL[2:4]) #  2이상, 4미만
print(numL[1:]) #   1번부터 끝까지
print(numL [:3])    #   처음부터 2번index까지
print(numL[:])  #   처음부터 끝까지
print(numL[1:-1])   #   1번부터 끝 바로 앞까지

#   리스트의 길이: len(리스트명)
print(len(list1))
print(len(list2))
print(len(list5))
print(len(numL))

#   특정요소 삭제: del(리스트명[n]) > 위치를 찾는다
aa = [100,200,300,400,500,600,700]
print(aa)
del(aa[1])
print(aa)
del(aa[3:5])
print(aa)

#   리스트 값 추가: 리스트.append(값)
aa = [100,200,300,400,500,600,700]
print(aa)
aa.append(800)
print(aa)
aa.append('숫자')
print(aa)
aa.append([1,2,3])
print(aa)

#   리스트에서 특정값 제거 > 특정값을 찾는다
#   리스트명.remove(값)
aa.remove(200)
aa.append(400)
aa.append(100)
aa.append(100)
print(aa)
aa.remove(100)  #   같은 값이 2개 이상이면 맨 앞에있는 숫자만 제거.

#   요소 확인방법: 내부에 요소가 포함되어 있는지 확인하기
#   in, not in >> True or False로 대답한다
print(100 in aa)
print(200 not in aa)

f = ['사과','딸기','복숭아','수박','배']
print('딸기' in f)

if '사과' in f :
    print('사과가 있습니다')
else:
    print('사과가 없습니다')
    
if '사과' not in f :
    print('사과가 없습니다')
else:
    print('사과가 있습니다')