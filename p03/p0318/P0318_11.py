class Student:
    stuCount = 0 #클래스변수
    stuNo = 0  #인스턴스변수 > 계속 변하는 변수

    # 생성자: __init__ initialize: 초기화
    # 클래스에 대한 객체선언을 하면 제일먼저 호출되는 함수
    def __init__(self,name="",kor=0,eng=0,math=0):   
        
        self.name = name
        if kor>100: #   점수가 100점이 넘어간다? 그럴수없지이
            self.kor = 100
        else:            
            self.kor = kor
            
        self.eng = eng
        self.math = math
        self.total = kor+eng+math    
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0
        Student.stuCount += 1  #   클래스변수선언 클래스명.변수명 
        self.stuNo = Student.stuCount
    def stu_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank,sep="\t")
    #   str 객체를 print하면 __str__함수를 제일먼저 호출한다
    def __str__(self):
        return f"{self.stuNo}{self.name}{self.kor}{self.eng}{self.math}{self.total}{self.avg}{self.rank}"
s1 = Student("홍길동",100,100,99)  #객체선언 > init이 호출된다, 아무것도 안들어있지만 init에 지정해두었다 그래서 에러안남.
s2 = Student("유관순",99,99,98)# 클래스명의 s2(참조변수)
s1.stu_print()
s2.stu_print()
print(s1)   #   str객체를 제일먼저 호출함.

