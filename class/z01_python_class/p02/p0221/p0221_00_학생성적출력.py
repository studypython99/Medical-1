#   변수명: stu_no, stu_name, kor, eng, math, total, avg, rank
#   출력:   번호    이름    국어    영어    수학    합계    평균    등수
#           1     홍길동    100    100     100     300   100.00    1
stu_no=input("번호를 입력하세요 >> ")
stu_name=input("이름을 입력하세요 >> ")
kor=int(input("국어점수를 입력하세요 >> "))
eng=int(input("영어점수를 입력하세요 >> "))
math=int(input("수학점수를 입력하세요 >> "))
rank=1
#   등수는...??
print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu_no,stu_name,kor,eng,math,(kor+eng+math),'%.2f'%((kor+eng+math)/3),rank))
