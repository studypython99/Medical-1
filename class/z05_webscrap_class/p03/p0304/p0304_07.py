students = [[1,'홍길동',100,100,100,300,100],
            [2,'유관순',100,100,100,300,100],
            [3,'이순신',100,100,100,300,100]] 
#            0    1     2   3   4   5   6
#                       국  영  수  합  평
while True:
    search = input('찾는 학생의 이름을 입력하세요 >>')
    chk = 0
    count = 0
    for stu in students:
        if search in stu:
            chk = 1
            break
        count += 1  #찾는 학생의 위치값
    if chk == 0 :
        print('찾는 학생의 정보가 없습니다.')
    else:
        print('입력한 학생 {}를 찾았습니다.'.format(search))
        print('[변경할 과목 선택]')
        num = int(input('1. 국어  2. 영어  3. 수학   0.취소 >>'))
        if num == 1:
            print('1. 국어를 선택하셨습니다.')
            print('현재 국어점수: {}'.format(students[count][2]))
            num = int(input('변경점수를 입력하세요 >>'))
            students[count][2] = num    #국어점수 만 변경되었으니, 합계, 평균도 포함되어야한다.
            print('국어점수가 변경되었습니다.')
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float('{:.2f}'.format(students[count][5]/3))
            print(students)
            print()
            #   성적수정 프로그램 구현
            
        elif num == 2:
            print('2. 영어를 선택하셨습니다.')
            print('현재 영어점수: {}'.format(students[count][3]))
            num = int(input('변경점수를 입력하세요 >>'))
            students[count][3] = num    #국어점수 만 변경되었으니, 합계, 평균도 포함되어야한다.
            print('영어점수가 변경되었습니다.')
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float('{:.2f}'.format(students[count][5]/3))    # str type 이다; 사칙연산에 적용 x 
            print(students)
            print()            
            #   성적수정 프로그램 구현
            
        elif num == 3:
            print('3. 수학을 선택하셨습니다.')
            print('현재 수학점수: {}'.format(students[count][4]))
            num = int(input('변경점수를 입력하세요 >>'))
            students[count][4] = num    #국어점수 만 변경되었으니, 합계, 평균도 포함되어야한다.
            print('수학점수가 변경되었습니다.')
            students[count][5] = students[count][2]+students[count][3]+students[count][4]
            students[count][6] = float('{:.2f}'.format(students[count][5]/3))
            print(students)
            print()                    
            #   성적수정 프로그램 구현
            
        elif num == 0:
            print('0. 취소를 선택하셨습니다.')
    