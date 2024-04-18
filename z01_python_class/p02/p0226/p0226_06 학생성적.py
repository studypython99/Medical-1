student = [[1,'홍길동',100,100,100,300,100.0,1],
           [2,'유관순',90,90,90,270,90.0,2]]

print('-'*35)
print('\t[학생성적프로그램]')
print('1. 학생성적입력')        #   1명만 입력 print(student)
print('4. 학생성적전체출력')    #   2명이 출력
print('-'*35)
ch = input('원하는 번호를 입력하세요 >>')   #   문자열형태, 숫자로 하고싶으면 int
stu3 = []
if ch == '1' :
    print('[학생 성적 입력]')
    name = input('이름을 입력하세요 >>')
    kor = int(input('국어점수 입력하세요 >>'))
    eng = int(input('영어점수 입력하세요 >>'))
    math = int(input('수학점수 입력하세요  >>'))
    total = kor+eng+math
    avg = total/3
    stu1 = [3,name,kor,eng,math,total,avg,3]
    student.append(stu1)
    print(student)
    
    # stu3.append(input('번호를 입력하세요 >>'))
    # stu3.append(input('이름을 입력하세요 >>'))
    # stu3.append(int(input('국어점수 입력하세요 >>')))
    # stu3.append(int(input('영어점수 입력하세요 >>')))
    # stu3.append(int(input('수학점수 입력하세요 >>')))
    # stu3.append(int(stu3[2]+stu3[3]+stu3[4]))
    # stu3.append(float(stu3[5]/3))
    # stu3.append(3)
    # print(stu3)
elif ch == '4' :
    print('[학생성적출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
    .format(student[0][0],student[0][1],student[0][2],student[0][3],
    student[0][4],student[0][5],student[0][6],student[0][7]))

else:
    print('다른 번호를 입력하세요')