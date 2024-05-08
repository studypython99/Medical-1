students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33, 'rank' : 1},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67, 'rank' : 1},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67, 'rank' : 1},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0, 'rank' : 1},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67, 'rank' : 1}
]
while True: #   while문이 두번 돌면, 마지막 break에도 멈추지 않는다!
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
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)

    cnt = len(students)+1
    if not choice.isdigit():
        print("숫자를 입력하세요.")
        continue
    choice = int(choice)
    # while True:
        #   1. 학생성적입력
    if choice == 1:
        while True:
            print('1. 학생성적입력')
            student = {}
            num = "S"+"{:03d}".format(cnt)
            student["stuNo"] = num
            name = input("이름 입력 (0. 취소)>>")
            if name == "0":
                break
            student["name"] = name
            kor = int(input("국어 입력 >>"))
            student["kor"] = kor
            eng = int(input("영어 입력 >>"))
            student["eng"] = eng
            math = int(input("수학 입력 >>"))
            student["math"] = math
            total = kor + eng + math
            student["total"] = total
            avg = total/3
            student["avg"] = float("{:.2f}".format(avg))
            print(student)
        
    #   2. 학생성적전체출력
    elif choice == 2:       
        print("2. 학생성적전체출력")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        for i in students:
            for j in i:
                print(i[j],end="\t")
            print()
        break
    
    #   3. 학생검색 출력
    elif choice == 3:
        print('3. 학생검색')
        search = input("이름입력 (0.취소) >>") 
        if search == "0":
            break
        elif search !=0:
            print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
            for stu in students:
                for i in stu:
                    if search in stu["name"]:
                        print(stu[i],end='\t')
        print()

    #   4. 학생수정, 학생의 위치를 알아야한다.
    elif choice == 4:
        s_title = [" ","국어","영어","수학"]
        print('4. 학생수정')
        search = input("이름입력 (0.취소)>>")
        if search == "0":
            break
        elif search !="0":
            s_input = int(input("수정할 과목 (1.국어 2.영어 3.수학) >>"))
            if s_input == 1:    #   국어
                score = int(input("{}점수 수정 >>".format(s_title[s_input])))
                print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                for stu in students:
                    for i in stu:
                        if search in stu["name"]:
                            stu["kor"] = score
                            stu["total"] = stu["kor"] + stu["eng"] + stu["math"]
                            stu["avg"] = stu["total"]/3
                            print(stu[i],end="\t")
                print()
            if s_input == 2:    #   영어
                score = int(input("{}점수 수정 >>".format(s_title[s_input])))
                print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                for stu in students:
                    for i in stu:
                        if search in stu["name"]:
                            stu["eng"] = score
                            stu["total"] = stu["kor"] + stu["eng"] + stu["math"]
                            stu["avg"] = stu["total"]/3
                            print(stu[i],end="\t")
                print()
            if s_input == 3:    #   수학
                score = int(input("{}점수 수정 >>".format(s_title[s_input])))
                print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
                for stu in students:
                    for i in stu:
                        if search in stu["name"]:
                            stu["math"] = score
                            stu["total"] = stu["kor"] + stu["eng"] + stu["math"]
                            stu["avg"] = stu["total"]/3
                            print(stu[i],end="\t")
                print()
            
    #   5. 등수처리
    elif choice == 5:
        print('5. 등수처리')
        ask = input("등수처리를 진행합니다 (1.진행 0.취소) >>")
        if ask == "0":
            break
        for i in students:
            rank = 1
            for j in students:
                if i["total"] < j["total"]:
                    rank += 1
                    i["rank"] = rank
        print("등수처리가 완료되었습니다.")
        break
                    
    #   6. 학생삭제
    elif choice == 6:
        print('6. 학생삭제')
        search = input("이름 입력 (0.취소) >>")
        if search == "0":
            break
        ask = input("{}학생의 성적을 삭제하시겠습니까?(1.진행 0.취소) >>".format(search))
        if ask == "0":
            print("취소되었습니다.")
            break
        elif ask != "0":
            for i, stu in enumerate(students):
                if search in stu["name"]:
                    del students[i]
                    print("{}학생의 성적이 삭제되었습니다.".format(search))
            
    #   7. 프로그램 종료
    elif choice == 0:
        print('0. 프로그램 종료')
        break


