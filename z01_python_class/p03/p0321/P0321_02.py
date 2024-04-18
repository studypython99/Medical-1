class Student:
    name = ""
    kor = 0
    total = 0
    
    def __init__(self,name="",total=0):
        self.name = name
        self.__total = total    #   프라이빗변수로 막아둠
    
    def __str__(self):
        return f"이름: {self.name}, 합계: {self.__total}"
    
    def set_total(self,total,login_id):  #프라이빗변수로 막아놓은걸 set 저장하는
        if login_id == "admin": #   접근권한이 있는 아이디만 들어온다.           
            self.__total = total
        else:
            print("접근권한이 없습니다.")
    
    def get_total(self):    #   get 
        return self.__total #이 함수 아니면 읽어올 수 없다.
    
    #   생성자가 없으면 init을 자동으로 만들어준다
    # def __init__(self) -> None:
    #     pass   #   <__main__.Student object at 0x0000022DBC731C40> 없어도 주소값을 알려준다.
    #   init을 만들면 매개변수 ()괄호 안에 데이터 갯수를 맞춰준다. 
    

    def stu_print(self):
        print("클래스 안에 있는 함수")
s = Student("홍길동",95)   #   객체선언!!할 때 무조건 init()함수 호출
s2 = Student("유관순",100)
print(s)
print(s2)

s.set_total(400,"admin")
print("get_total: ",s.get_total())
def stu_print():
    print("클래스 밖에 있는 함수")
    
class Lotto:    
    pass

    
print(s)            #   <__main__.Student object at 0x0000022DBC731C40>

print(Student())    #   <__main__.Student object at 0x0000027EF17D1AF0> 다른 저장장소

#   클래스 내부에 있는 함수는 self 가 붙어있다. 
#   클래스 내부에 있는 함수는 객체선언을 해야 사용할 수 있다.

s.stu_print()   #   클래스 내에 있는 함수는 꼭 객체선언을 해야 사용가능 객체선언: s=Studnet()
stu_print()
#-------------------------------------------------------------------------------------------
if isinstance(s2,Student):
    print("Student 클래스 변수입니다.")
elif isinstance(s2,Lotto):
    print("Lotto 클래스 변수입니다.")

s.total = 300
print(s)