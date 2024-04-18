#   리스트를 사용해서 출력
stu1 = [1,'홍길동',100,100,100,300,100.0,1]
stu2 = [2,'유관순',90,90,90,270,90.0,2]
stu3 = []
print('[학생 성적 출력]')
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu1)) # *리스트 = 요소를 전개한다.
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu2))

choice = int(input('원하는 번호를 입력하세요 >>'))
if choice == 1 :
    print('1. 학생성적입력')
    stu3.append(input('번호를 입력하세요 >>'))
    stu3.append(input('이름을 입력하세요 >>'))
    stu3.append(int(input('국어점수를 입력하세요 >>')))
    stu3.append(int(input('영어점수를 입력하세요 >>')))
    stu3.append(int(input('수학점수를 입력하세요 >>')))
    stu3.append(int(stu3[2]+stu3[3]+stu3[4]))
    stu3.append(int(stu3[5]/3))
    stu3.append(input('등수를 입력하세요 >>'))
elif choice == 4 :
    print('4. 학생성적전체출력')
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu1))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu2))
elif choice == 0 :
    print('프로그램종료')

print('[학생 성적 출력]')
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu1))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu2))
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu3))
