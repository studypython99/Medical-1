#   학생성적 입력

#   변수를 사용합니다
stu_name = '홍길동'
kor = 100
eng = 100
math = 100

#   입력을 받아서 총점과 평균을 계산하고,

#   출력해보세요
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print(''.format())

num = int(input('번호를 입력하세요 >>')) #번호를 입력하고, 그 번호가 1이면
list1 = []  # 1이면, 여기에 저장하도록
list2 = []

if num == 1 :
    list1.append(num)
    list1.append(input('이름을 입력하세요 >>'))
    list1.append(int(input('국어성적을 입력하세요 >>')))
    list1.append(int(input('영어성적을 입력하세요 >>')))
    list1.append(int(input('수학성적을 입력하세요 >>')))
    list1.append(list1[2]+list1[3]+list1[4])
    list1.append(list1[5]/3)
    list1.append('rank')
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print(list1)
elif num == 2 :
    list2.append(num)
    list2.append(input('이름을 입력하세요 >>'))
    list2.append(int(input('국어성적을 입력하세요 >>')))
    list2.append(int(input('영어성적을 입력하세요 >>')))
    list2.append(int(input('수학성적을 입력하세요 >>')))
    list2.append(list2[2]+list2[3]+list2[4])
    list2.append(list2[5]/3)
    list2.append('rank')
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print(list1)
    print(list2)
else:
    print('성적 입력을 마치시겠습니까?')
    
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print(list1)
print(list2)