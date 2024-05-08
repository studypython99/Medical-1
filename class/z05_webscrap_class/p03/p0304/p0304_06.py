students = [[1,'홍길동',100,100,100,300,100],
            [2,'유관순',100,100,100,300,100],
            [3,'이순신',100,100,100,300,100]] 

#   찾는 학생의 이름

#   찾고자 하는 학생 찾기
while True:
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
        
        #     elif ch == 3:
        # check = 0
        # print('3. 검색 출력')   #   이름을 입력하면 해당 리스트를 보여준다.
        # sch_name = input('이름을 입력하세요 >>')
        # for stu in member:      #   1에서 입력한 내용들 중에서
        #     if sch_name in stu: #   검색한 이름이 있으면
        #         check = 1
        #         print('{}이 존재합니다.'.format(sch_name))
        #         print(stu)
        # if check == 0:
        #     print('존재하지 않습니다.')
        #     # else:
        #     #     print('{}이 존재하지 않습니다.') >> 이상태에서는 {}존재하지않습니다가 stu만큼 출력된다.