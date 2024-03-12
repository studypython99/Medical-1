# n = int(input('원하는 번호를 입력해주세요 >>')) #   n은 문자열
# print(n)

# if n.isdigit(): #   숫자 이지만 문자열 ex) '0', "2"
#     n = int(n)  #   숫자만 입력한걸 확인해주는 검열장치
# else:
#     print('문자가 입력되었습니다. 다시 입력해주세요.')

#   이름을 검색해보고, 이름을 검색해서 삭제
students = [[1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],[4,'김유신',70],[5,'김구',95]]

while True:
    print('1. 학생 검색')
    print('2. 학생 삭제')
    print('3. 프로그램 종료')
    ch = input('원하는 번호를 입력해주세요 >>')
    if ch.isdigit():    # 입력한 내용이 숫자면 True
        ch = int(ch)
    if ch == 1:
        search_name = input('검색할 학생의 이름을 입력해주세요 >>')
        chk = 0 #   체크변수
        for stu in students:    #   [1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],[4,'김유신',70],[5,'김구',95]
            if search_name in stu:  # 2차 리스트 중 1차 리스트의 내용을 확인
                print('{} 학생이 존재합니다.'.format(search_name))
                print(stu)
                chk = 1 #   체크변수를 1로 바꿈, 이게 없으면.. 뭘 할까?
        if chk == 0:
            print('검색 학생이 존재하지 않습니다.')
    elif ch == 2:
        del_name = input('삭제 할 학생의 이름을 입력해주세요 >>')
        chk = 0 # 학생이 없으면 0, 있으면 1 / 여기에선 있다.
        for i, stu in enumerate(students):  # stu는 i번째에 있습니다. 요소1, 요소2, 요소3, ...
            if del_name in stu:
                del(students[i])
                chk = 1 # 0 > 1 로 바뀌었다? 
                print(del_name,'학생이 삭제되었습니다.')
        if chk == 0:    # 0 에 걸렸다?
            print('검색 학생이 존재하지 않습니다.')
        print(students)
    elif ch == 3:
        print('프로그램이 종료되었습니다.')
        break
    else:
        print('숫자를 입력하세요. 다시 입력하세요.')