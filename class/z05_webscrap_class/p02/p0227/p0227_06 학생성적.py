stu = []


for i in range(10):  #  for를 사용해서 10번 반복
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input('원하는 숫자를 입력하세요 >>')
    if ch == '1' :
        print('1. 학생성적입력')
        num = input('번호를 입력하세요 >>')
        name = input('이름을 입력하세요 >>')
        kor = int(input('국어성적을 입력하세요 >>'))
        eng = int(input('영어성적을 입력하세요 >>'))
        math = int(input('수학성적을 입력하세요 >>'))
        total = kor+eng+math
        avg = total/3
        st = [num,name,kor,eng,math,total,avg]
        stu.append(st)
    elif ch == '4' :
        print('4. 학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
        for i in range(len(stu)) :
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}'
            .format(stu[i][0],stu[i][1],stu[i][2],stu[i][3],stu[i][4],stu[i][5],stu[i][6]))
    elif ch == '0' :
        print('프로그램을 종료합니다.')
    else:
        print('다른 번호를 입력하세요.')