#   리스트
#   대괄호로 감싸서 나타내며 0개 이상의 원소가 저장될 수 있스니다.
num = 1
num = 2
print(num)

listA = [1,2]
listB = []

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
#   지금까지는 이렇게 하나씩 했다.

list1 = [1,2,3,4,5]
list2 = ['사과', '복숭아', '딸기', '배', '포도', '수박']
#           0       1       2       3     4       5
list3 = [1,'홍길동', 100,3.14,-3]   #정수, 문자, 실수 혼합도 가능

print(list2) # ['사과', '복숭아', '딸기', '배', '포도', '수박']
print(list2[1])
print(list1[3]) #   4
print(list3[3]) #   3.14
print(list2[-1]) #  뒤에서부터 -1,-2,-3,-4.......

#   리스트의 길이 출력
a = len(list2)
print(a)
print(len(list2))

#   list2에서 딸기를 출력해보세요
print(list2[2])

#리스트 슬라이싱
aa = [0,1,2,3,4,5,6,7,8,9,10]
print(aa) # = print(aa[:])
print(aa[1:4])  #   1이상 4미만: [1,2,3]
print(aa[3:8])  #   3이상 8미만: [3,4,5,6,7]
print(aa[2:])   #   2이상 모두: [2,3,4,5,6,7,8,9,10]
print(aa[:7])   #   처음부터 7미만: [0,1,2,3,4,5,6]

#   요소확인: 내부에 포함되어 있는지 확인하는 방법을 ㅈ공해줌
#   in, not in > True, False
print('포도' in list2)
print(11 in aa)
print(0 not in aa)

listC = (1, 2,  3,['a','b','c'],[4,5])
#        0  1   2       3        4
print(1 in listC)   #   True
print(4 in listC)
