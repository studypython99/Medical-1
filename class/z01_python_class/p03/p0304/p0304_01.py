#   https://app.slack.com/client/T06KYJGBQ1K?selected_team_id=T06KYJGBQ1K 슬랙

students = []    #   학생성적 저장
cnt = 0 #   번호입력
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생정렬')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >>')
    # if ch.isdigit():    # 입력한 내용이 숫자면 True
    #     ch = int(ch)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue    #   반복문 다시 실행
    choice = int(choice)
#   1. 학생성적입력 프로그램
    if choice == 1:
        while True:     #   성적입력만 계속 진행하고싶다
            print('학생성적을 입력합니다.')
            print('-'*10)
            student = []
            name = input('이름을 입력하시오.(-1. 취소)')
            if name == '-1':
                break
            cnt += 1
            student.append(cnt)
            student.append(name)
        #   kor = int(input('국어점수를 입력하세요.))       #   이렇게도 가능
            student.append(int(input('국어점수를 입력하시오.')))   
            student.append(int(input('영어점수를 입력하시오.')))
            student.append(int(input('수학점수를 입력하시오.')))
            sum = student[2]+student[3]+student[4]  #   students[0] = 학번, student[1] = 이름
            student.append(sum)     #   합계저장
            student.append('{:.2}'.format(sum/3))     #   평균저장
            students.append(student)
            print(students)         #   전체학생 출력
#   2. 학생성적전체출력 프로그램
    elif choice == 2:
        print('[학생성적 출력]')
        print('-'*50)
        print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        for stu in students:
            for s in stu:
                print(s,end='\t')
            print()
        print('-'*50)
#   3. 학생검색 프로그램
    elif choice == 3:
        search = input('검색하고 싶은 학생 이름을 입력하세요.(0. 취소)')
        check = 0   #   찾는 정보확인
        if search == '0':
            break
        for stu in students:
            if stu[1] == search:
                check = 1   #   정보를 찾았을 때 정보확인을 1로 변경
                break
        if check == 1:
            print('{}의 학생정보를 찾았습니다.'.format(search))
            
        else:
            print('찾는 학생이 없습니다.')
#   4. 학생수정 프로그램
    elif choice == 4:
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
#   5. 등수처리 프로그램
    elif choice == 4:
        choice = input('등수처리를 실행하시겠습니까?(1.실행, 0.취소)')
    if choice == '0':
        print('등수처리를 취소하셨습니다.')
        break
    else:
        #   등수처리 진행
        for i_stu in students:
            no = 1                          #   초기화
            for j_stu in students:
                if i_stu[5] < j_stu[5]:     #   각각의 총합 비교
                    no += 1                 #   비교대상 총합이 더 크면 1 증가
            i_stu[7] = no                       #   등수 위치에 no저장
    print('등수처리가 완료되었습니다.')
    print('-'*40)
    print('[등수확인]')
    print(students)
        #   0. 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break   #   반복문 종료 

    
    
