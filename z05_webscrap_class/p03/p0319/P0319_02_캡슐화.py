class Car:
    # color = ""    init에 있어서 삭제 가능
    # door = 5
    # tire = 4
    # speed = 0
    
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed #  
        
    def up_speed(self,smartKey):
        if smartKey == "0x1100":
            self.__speed += 10
    def down_speed(self):
        self.__speed -= 10  #__speed << 캡슐화, 접근제한을 건다.
                            #   클래스 내부에서만 접근이 가능하게 만듦.

    def get_speed(self)        :
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed += speed
c1 = Car("white",5,4,0) #   speed = 0
c1.up_speed("0x1100")#   speed = 10 스마트키True
c1.up_speed("0x1101")#   speed = 20 스마트키False
c1.set_speed(500)
#c1.speed = 300 갑자기 속도만 300으로? 이런걸 막는 __speed
# print(c1.speed) #   'Car' object has no attribute 'speed' 스피드접근금지
print(c1.get_speed()) #접근이 가능하다
c2 = Car("red",4,4,0)