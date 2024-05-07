#   학생성적프로그램
num = input('번호 >> ')
name = input('이름 >> ')
kor = int(input('국어 >> '))
eng = int(input('영어 >> '))
math = int(input('수학 >> '))
total = int((kor+eng+math))
avg = int(total/3)
print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(num,name,kor,eng,math,total,avg))
if avg >= 60:
    print('{}님 평균 {}점으로 합격입니다.(기준:60점)'.format(name,avg))
else:
    print('{}님 평균 {}점으로 불합격입니다.(기준:60점)'.format(name,avg))