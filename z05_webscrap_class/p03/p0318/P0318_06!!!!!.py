class Student:
    # stuNo = 0   #   init self 사용시 class 정의 사용 안해도 ok
    # stu_name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    
    def __init__(self,stuNo=0,stu_name="",kor=0,eng=0,math=0):
        self.stuNo = stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        
#   1,홍길동,99,99,87,285,95.0,1
stu1 = Student(1,"홍길동",99,99,87,285,95.0,1)
print(stu1.stuNo,stu1.stu_name,stu1.kor,stu1.eng,stu1.math,stu1.total,stu1.avg,stu1.rank)
#   2,유관순,98,93,87,278,92.67,3
stu2 = Student(2,"유관순",98,93,87,278,92.67,3)
print(stu2.stuNo,stu2.stu_name,stu2.kor,stu2.eng,stu2.math,stu2.total,stu2.avg,stu2.rank)
#   3,이순신,88,76,30,194,64.67,6
stu3 = Student(3,"이순신",88,76,30,194,64.67,6)
print(stu3.stuNo,stu3.stu_name,stu3.kor,stu3.eng,stu3.math,stu3.total,stu3.avg,stu3.rank)

stu4 = Student()
stu4.stuNo = 4
stu4.stu_name = "홍길순"
stu4.kor = 100
stu4.eng = 100
stu4.math = 100
stu4.total = 300
stu4.avg = 100
stu4.rank = 2
print(stu4.stuNo,stu4.stu_name,stu4.kor,stu4.eng,stu4.math,stu4.total,stu4.avg,stu4.rank)