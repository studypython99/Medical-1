import os   #   파일 불러오기
class Student:  #   클래스 선언
    count = 1
    def __init__(self,name,kor, eng, math,stuNo=0,rank=0):
        if stuNo == 0:          # stuNo=0 키워드변수
            self.stuNo = Student.count #클래스변수 사용
        else:
            self.stuNo = stuNo
        self.stuNo = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        if rank !=0:
            self.rank = rank

    def __str__(self):  #프린트해서 출력해줌
        return f"학생성적:{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
            
students = []
        
#   파일 불러오기
f = open("stu.txt","r",encoding="utf8")
#   파일 읽기
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    #   1,홍길동,100,99,87,286,95.33,2
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
    
#   리스트 출력
for stu in students:
    print(stu)
    
f.close()