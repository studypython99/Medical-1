import stu_file
students = stu_file.stu_open() #stu_file의 stu_open()함수 호출
s_title = ['','국어','영어','수학']

# 1. 학생성적입력 함수
def stu_insert(cnt):
    while True :
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요 (0.취소)>>")
        if name == '0':
            print("학생입력을 취소합니다.")
            break
        student = {}    #   데이터 초기화
        student["stuNo"] = cnt
        student["name"] = name          #    딕셔너리 추가
        kor = int(input("국어점수 입력하세요 >>"))
        student["kor"] = kor
        eng = int(input("영어점수 입력하세요 >>"))
        student["eng"] = eng
        math = int(input("수학점수 입력하세요 >>"))
        student["math"] = math
        total = kor+eng+math
        student["total"] = total
        avg = total/3
        student["avg"] = float('{:.02f}'.format(avg))
        students.append(student)
        cnt += 1
        print(student)
        print(students)

#   2. 학생성적출력 함수
def stu_grade_print(students):
    print(('[학생성적전체출력]'))
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
    for i in students:
        # print(i)    #   i = student[{0번째},{1번째}..{n번째}]
        for j in i:
            print(i[j],end="\t")    #   dict 형태일 때, i 키의 [j] 벨류값을 가져온다. 
        print()
        
#   3. 학생검색출력 프로그램
def stu_search_print(students):
    while True:
        print('3. 학생검색')
        search = input("이름 입력(0. 취소) >>")
        if search == "0": break
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        for stu in students:
            for i in stu:
                if search in stu["name"]:
                    print(stu[i],end='\t')
        print()
        
#   4. 학생수정 프로그램
def stu_update():
    while True:
            search = input('찾을 학생의 이름을 입력하세요 (0.취소)>>')
            chk = 0
            if search == '0':
                break
            for i in students:
                if i['name'] == search:
                    break
                chk += 1
            
            print("찾고자 하는 학생의 위치:",chk)
            if chk == len(students):    #   학생수만큼 for문을 돌면
                print(f"{search} 학생은 없습니다. 다시 입력하세요.")
                
                
            else:
                print(f"{search} 학생을 찾았습니다.")
                while True:
                    
                    print("1.국어\t2.영어\t3.수학")
                    s_input = int(input("수정하려는 과목을 선택하세요 (0.취소) >>"))
                    if s_input == 0: break
                    
                    #   국어수정
                    elif s_input == 1:
                        s_1 = "kor"
                        stu_sub(s_input,chk,s_1)
                        
                    #   영어수정
                    elif s_input == 2:
                        s_1 = "eng"
                        stu_sub(s_input,chk,s_1)
                    
                    #   수학수정
                    elif s_input == 3:
                        s_1 = "math"
                        stu_sub(s_input,chk,s_1)
                        
                    else:
                        print("과목수정을 취소합니다.")
                        break
                    
#   4-1. 과목수정 프로그램
def stu_sub(s_input,chk,s_1):
    print("[{}수정]".format(s_title[s_input]))
    print("현재 {}점수: {}".format(s_title[s_input],students[chk][s_1]))
    print('-'*20)
    score = int(input("수정할 {}점수를 입력하세요 >>".format(s_title[s_input])))
    students[chk][s_1] = score
    #   합계수정
    students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
    students[chk]['avg'] = float("{:.2f}".format(students[chk]['total']/3))
    print("{}점수: {}점으로 수정되었습니다.".format(s_title[s_input],students[chk][s_1]))
    print(students[chk])
#---------------------------------------------------------------------------------------
cnt = len(students)+1
# 학생번호 사용
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
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1 :
        stu_insert(cnt)
        
    # 2. 학생성적전체출력 프로그램
    elif choice == 2 :
        stu_grade_print(students)
        
    # 3. 학생검색출력 프로그램
    elif choice == 3 :
        stu_search_print(students)
    
    # 4. 학생성적수정 프로그램
    elif choice == 4:
        stu_update()
        
    # 5. 등수처리 프로그램
    elif choice == 5:
        for i, s_dic in enumerate(students):
            rank_cnt = 1    #   등수처리 변수
            for i_dic in students:
                if s_dic['total'] < i_dic['total']:
                    rank_cnt += 1
            s_dic['rank'] =rank_cnt
        print('등수처리가 완료되었습니다.')
        print(students)
        
        
    elif choice == 6:
        while True:
            search = input('찾을 학생의 이름을 입력하세요 (0.취소)>>')
            chk = 0
            if search == '0':
                break
            for i in students:
                if i['name'] == search:
                    break
                chk += 1
            
            print("찾고자 하는 학생의 위치:",chk)

            if chk >= len(students):
                print("찾는 학생이 없습니다.")
            else:
                print("{} 학생을 찾았습니다.".format(search))
                s_input = (input("{} 학생 성적을 삭제하시겠습니까? (0.취소)".format(search)))
                #   삭제
                if s_input != '1':
                    print('삭제를 취소합니다.')
                    #break??
                else:
                    del students[chk]
                    print('{}학생의 성적이 삭제되었습니다.'.format(search))
    elif choice == 0:
        print('프로그램을 종료합니다.')