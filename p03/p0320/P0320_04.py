class Student:
    name = ""
    total = 0
    
    def __init__(self,name,total):
        self.name = name
        self. total = total

    def __str__(self):
        return f"이름: {self.name}, 총점: {self.total}"
    
    def __del__(self):  #   사용을 안할 때
        return "클래스가 소멸될 때 실행"
    
    def __add__(self,s): #  더하게 되는 상황에서 제일먼저 호출됨.
        return self.total+s.total
     
    def __gt__(self,s):    #크거나 같다라고 비교할 때
        print("클래스간 비교를 하면 이 함수가 호출")    
    
    def __eq__(self,s):     #   내부함수
        return self.name == s.name and self.total == s.total
            
s1 = Student("홍길동",100)
s2 = Student("유관순",90)
s3 = Student("이순신",95)
s4 = Student("홍길동",100)

print(s1)   #   주소값 출력 <__main__.Student object at 0x0000025944821E80>
            #   def __str__ 추가 후
            #   이름: 홍길동, 총점: 100

print("s1: ",s1)            #   이름: 홍길동, 총점: 100
print("s1+s1: ",s1+s2)      #   190

print(s1>s2)
print(s1)
print(s4)
print(s1==s4)   #   false, 주소로 비교하니 다르다. 주소값이,,
                #   __eq 설정 후 True
print(s1==s2)   #   False