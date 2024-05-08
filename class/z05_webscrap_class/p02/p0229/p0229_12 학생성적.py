students = []
count = 0 # ??? 뭐더라...;;
while True: #   무한반복을 합니다. 입력 > 출력 > 검색 > 삭제 > 수정
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 입력')        #   이름,국영수를 입력받으면 [이름,국영수,합,평]
    print('2. 수정')        #   국영수 점수수정 합,평도 같이 바뀌어야한다
    print('3. 삭제')        #   도전
    print('4. 전체출력')    
    print('5. 검색출력')    #   도전
    print('6. 등수처리')    #건너뛰기
    print('0. 프로그램종료')    #   break
    print('-'*35)
    choice = input('원하는 번호를 입력하세요 >>')
    print('입력하신 번호는 {}입니다.'.format(choice))
    if choice == '1':
        print('1. 입력')
        name = input('이름을 입력하세요 >>')
        kor = int(input('국어점수 >>'))
        eng = int(input('영어점수 >>'))
        math = int(input('수학점수 >>'))
        total = kor+eng+math
        avg = total/3
        stu_info = [name,kor,eng,math,total,avg]
        students.append(stu_info)
    elif choice == '2':
        print('2. 수정')        #   국영수 점수수정 합,평도 같이 바뀌어야한다
    elif choice == '3':
        print('3. 삭제')        #   도전
    elif choice == '4':
        print('4. 전체출력')
        print('이름\t국어\t영어\t수학\t합계\t평균')
        for i in range(len(students)):   #   입력한 요소의 수만큼 i = 0,1,2,3,.....
            print('{}\t{}\t{}\t{}\t{}\t{}'
                  .format(students[i][0],students[i][1],students[i][2],students[i][3],
                          students[i][4],students[i][5]))
    elif choice =='5':
        print('5. 검색출력')    #   도전
        search_name = input('이름을 입력하세요 >>')
        for i, stu in enumerate(students):
            if search_name in stu:
                print('이름\t국어\t영어\t수학\t합계\t평균')
                print('{}\t{}\t{}\t{}\t{}\t{}'
                  .format(students[i][0],students[i][1],students[i][2],students[i][3],
                          students[i][4],students[i][5]))
    elif choice == '6':
        print('6. 등수처리')    #건너뛰기
    elif choice == '0':
        print('0. 프로그램종료')    #   break
        print('프로그램을 종료합니다.')
        break