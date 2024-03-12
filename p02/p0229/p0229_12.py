member = []
i = 0
#   이름을 입력받아서 [[1,'홍길동'],[2,'이순신'],[3,'유관순]]
while True:
    print('-'*25)
    print('1. 입력')
    print('2. 전체 출력')
    print('3. 검색 출력')
    print('4. 검색 삭제')
    print('5. 검색 수정')
    print('0. 종료')
    ch = input('원하는 번호를 선택하세요 >>')
    print('-'*25)
    ch = int(ch)
    if ch == 1:
        i += 1
        print('1. 입력')    #   입력할때마다 1홍길동, 2이순신, 3유관순 되도록 1씩 증가하도록
        name = input('이름을 입력하세요 >>')
        m = [i, name]   #   입력을 누를때만 (ch = 1) 증가하고 다른번호에서는 증가하지 않도록
        member.append(m)
        print(member)
    elif ch == 2:
        print('2. 전체 출력')
        print('번호\t이름') #   [[1,'홍길동'],[2,'이순신'],[3,'유관순]]
        for i in range(len(member)):    #   i = 0,1,2,3
            print('{}\t{}'.format(member[i][0],member[i][1]))
    elif ch == 3:
        check = 0
        print('3. 검색 출력')   #   이름을 입력하면 해당 리스트를 보여준다.
        sch_name = input('이름을 입력하세요 >>')
        for stu in member:      #   1에서 입력한 내용들 중에서
            if sch_name in stu: #   검색한 이름이 있으면
                check = 1
                print('{}이 존재합니다.'.format(sch_name))
                print(stu)
        if check == 0:
            print('존재하지 않습니다.')
            # else:
            #     print('{}이 존재하지 않습니다.') >> 이상태에서는 {}존재하지않습니다가 stu만큼 출력된다.
    elif ch == 4:
        print('4. 검색 삭제')
        del_name = input('이름을 입력하세요 >>')
        # for stu in member:            >>> 삭제할 때 번호부여가 안되어있으면 요소 삭제가 어렵다..?
        #     if sch_name in stu:           번호 부여를 위해 enumerate 사용
        for i, stu in enumerate(member):    #   stu는 i번째에 있습니다. 요소1, 요소2, 요소3, ...
            if del_name in stu:
                del(member[i])              # i 가 계속 따라오더라...
                print(del_name,'님이 삭제되었습니다.')
    elif ch == 5:
        print('5. 검색 수정')
        '''
        누구의 정보를 수정할지 > 누구 정보를 수정할까요
        번호, 이름
        번호를 수정, 이름을 수정,
        만약에 번호를 수정한다면 수정될 값 1 > 6
        이름을 수정한다면 홍길동 > 유관순
        '''
        re_name = input('수정할 이름을 입력하세요 >>')
        for i , stu in enumerate(member):
            if re_name in stu:  #   이름이 있다면
                print(re_name,'님을 선택하셨습니다.')
                change_info = input('수정하실 항목을 선택하세요 >>\n(1.번호수정 / 2.이름수정)')
                if change_info == '1':
                    print(re_name,'님의 번호수정을 선택하셨습니다.')
                    print(re_name,'님의 번호는',member[i][0],'입니다.')
                    #   수정하는 코드 입력을 받아서 수정하기
                    stu_num = input('새로운 번호를 입력해주세요 >>')
                    stu_num = int(stu_num)
                    member[i][0] = stu_num
                elif change_info == '2':
                    stu_name = input('새로운 이름을 입력해주세요 >>')
                    member[i][1] = stu_name
    elif ch == 0:
        print('0, 종료')