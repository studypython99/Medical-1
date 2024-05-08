student = []
#   for를 사용해서 5번 반복
for i in range(5):
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input('원하는 번호를 입력하세요 >>')
    print(ch)
    #   if문을 사용해서 1 누르면 [학생성적입력]
    if ch == '1' :
        print('1. 학생성적입력')
        num = input('번호를 입력하세요 >>')
        name = input('이름을 입력하세요 >>')
        kor = int(input('국어점수 입력하세요 >>'))
        eng = int(input('영어점수 입력하세요 >>'))
        math = int(input('수학점수 입력하세요  >>'))
        total = kor+eng+math
        avg = total/3
        stu1 =[num,name,kor,eng,math,total,avg]
        student.append(stu1)
        
    #   4 누르면 [학생성적전체출력]
    elif ch == '4' :
        print('4. 학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수') #이걸 for 문으로 받아라!?
        for i in student :
            print(student)
        
        
        
    #     print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수') #이걸 for 문으로 받아라!?
    #     print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    #     student[0][0],student[0][1],student[0][2],
    #     student[0][3],student[0][4],student[0][5],
    #     student[0][6],student[0][7])) # 홍길동
    #     print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    #     student[1][0],student[1][1],student[1][2],
    #     student[1][3],student[1][4],student[1][5],
    #     student[1][6],student[1][7])) # 홍길동  
    # #   0 누르면 [프로그램 종료]
    elif ch == '0' :
        print('0. 프로그램 종료')
    else:
        print('다른 번호를 입력하세요')
        