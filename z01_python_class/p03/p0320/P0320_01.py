class Car:
    # color = ""
    # speed = 0
    count = 0   #   클래스변수로 인식, 인스턴트변수로도 사용 가능(하지만 오해의 소지가 있을 수 있다....!?)
    
    def __init__(self,color="",speed=0): #기본값 init 설정, 인스턴스변수로 인식
        self.speed = speed
        self.color = color              #   생성자: 인스턴트를 생성하면서 필드값을 초기화시킨다.
        
#   class 사용하기 위해서는 인스턴스 선언
c1 = Car()        # 인스턴스 선언!! 선언 없이는 클래스를 사용할 수 없다ㅏㅏ
#   TypeError: Car.__init__() missing 2 required positional arguments: 'color' and 'speed'
#   Car() 괄호 안에 매개변수 color, speed를 맞춰줘야 하는데 아무것도 없어서 생기는 에러.
#   초기화 해주려면 init__(self,color="",speed=0) 기본값 설정
c1.color = "white"
print("c1.color: ",c1.color)
print("c1.seppd:",c1.speed)
Car.count = 10  #   클래스변수 자체에 10을 입력
print("c1.count: ",Car.count )

c2 = Car()
c2.color = "red"
print("c2.color: ",c2.color)
print("c1.color: ",c1.color)
# c2.count = 100                #   클래스class 변수를 인스턴트init 변수로 사용하지 말라
# print("c1.count: ",c1.count) 
# print("c2.count: ",c2.count) 
c1.count = 1    # c1,c2의 값을 따로 하면 따로값을 갖는다
c2.count = 2
Car.count = 100
print("c1.count: ",c1.count)    #   1
print("c2.count: ",c2.count)    #   2
print("Car.count: ",Car.count)  #   100
c3 = Car()  #   Car.count 값을 가져온다. class count 소환
print("c3.count: ",c3.count)    #   100

c2.door = 4
print("c2.door:",c2.door)   #   없는 옵션이지만 추가해서 입력 가능하다
