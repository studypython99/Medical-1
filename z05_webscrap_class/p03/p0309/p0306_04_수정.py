students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt = len(students)+1
print(cnt)
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')  
    print('-'*40)
    choice = input('프로그램 번호를 입력하세요 >>')
    print('-'*40)
    if not choice.isdigit():
        print("숫자만 입력하세요.")
        continue
    choice = int(choice)
    
    #   4. 수정
    if choice == 4:
        s_title = ['','국어','영어','수학']
        while True:
            print('4. 학생수정')
            search = input("이름 입력 (0.취소)>>")
            chk = 0
            for s_dic in students:
                if s_dic["name"] == search:
                    break                    
                chk += 1  
            s_input = int(input("수정할 과목 (1.국어 2.영어 3.수학) >>"))
            if search == "0":
                break
            elif s_input == 1:
                s_1 = "kor"
                print("현재 {}점수: {}".format(s_title[s_input],students[chk][s_1]))
                score = int(input("수정할 점수 >>"))
                students[chk][s_1] = score
                #   합계수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print(students[chk])
            elif s_input == 2:
                s_1 = "eng"
                print("현재 {}점수: {}".format(s_title[s_input],students[chk][s_1]))
                score = int(input("수정할 점수 >>"))
                students[chk][s_1] = score
                #   합계수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print(students[chk])
            elif s_input == 3:
                s_1 = "math"
                print("현재 {}점수: {}".format(s_title[s_input],students[chk][s_1]))
                score = int(input("수정할 점수 >>"))
                students[chk][s_1] = score
                #   합계수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print(students[chk])
                