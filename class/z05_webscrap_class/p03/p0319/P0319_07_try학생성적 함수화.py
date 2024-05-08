class Student:
    count = 1   #   클래스 변수 사용
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count  # 클래스변수 사용
        else:            
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank
    def __str__(self):  #   객체를 호출하면 출력
        return  f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"
#   파일 불러와서 저장하기------------------------------------------------------------------

students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break     #   모두 다 읽어왔으면 끝.
    txt_list = txt.split(",")   #읽어온걸 , 으로 구분짓는다
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()
Student.count = len(students)+1
print(s.name,s.stuNo) # 홍길순, 6

#   함수부분-------------------------------------------------------------------------------
#   프로그램-------------------------------------------------------------------------------
while True:    
    print("-"*40)
    print("[학생성적입력프로그램]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색출력")
    print("4. 학생성적수정")
    print("5. 등수처리")
    print("6. 삭제")
    print("0. 종료")
    print("-"*40)
    choice = input("번호를 입력하세요 >>")
    choice = int(choice)
    if choice == 1:
        print("1. 학생성적입력")
        name = input("이름입력(0.취소) >>")
        if (name == "0"): 
            print("입력을 취소합니다.")
            break
        kor = int(input("국어 입력 >>"))
        eng = int(input("영어 입력 >>"))
        math = int(input("수학 입력 >>"))
        #   list에 추가
        s = Student(name,kor,eng,math)
        students.append(s)
        print("입력데이터: ",s)
    
    elif choice == 2:    
        print("2. 학생성적전체출력")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        for i in students:
            print(i)
    
    elif choice == 3:
        print("3. 학생검색출력")
        search = input("이름 입력 >>")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        for i in students:
            if i.name == search:
                print(i)
        print()
        
    elif choice == 4:   #   cnt 설정으로 학생위치 확인
        print("4. 학생성적수정")
        search = input("이름 입력 >>")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        cnt = 0
        for i,m in enumerate(students):
            if m.name == search:
                print(i)
            cnt += 1
            print("1.국어 2.영어 3.수학 0.취소")
            choice = int(input("수정할 과목 선택 >>"))
            if choice == 0: break
            elif choice == 1:
                students[cnt].kor = int(input("점수 입력 >>"))
                students[cnt].total = students[cnt].kor + students[cnt].eng +students[cnt].math
                students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
            elif choice == 2:
                students[cnt].eng = int(input("점수 입력 >>"))
                students[cnt].total = students[cnt].kor + students[cnt].eng +students[cnt].math
                students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
            elif choice == 3:
                students[cnt].math = int(input("점수 입력 >>"))
                students[cnt].total = students[cnt].kor + students[cnt].eng +students[cnt].math
                students[cnt].avg = float("{:.2f}".format(students[cnt].total/3))
                
    elif choice == 5:        
        print("5. 등수처리")
        print("1.진행 0.취소")
        choice = int(input("번호 입력 >>"))
        if choice == 1:
            for s in students:
                rank_count = 1
                for ss in students:
                    if s.total < ss.total:
                        rank_count += 1
                    s.rank = rank_count
            print("등수처리가 완료되었습니다.")
            
        
    
        print("6. 삭제")
        print("0. 종료")