class Car:
    # color = "white"
    # speed = 0
    
    count = 0
    
    def __init__(self,color="white",door = 5,tire = 4,speed=0) -> None:
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        
    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed -= 10
        
    def stop_speed(self):
        self.speed = 0
        
class Ambul_car(Car):#  상속: Car클래스의 모든것을 가져온다.
    
    def up_speed(self):
        self.speed += 20    # 오버라이딩, 부모의 함수를 '재정의'한다.
        
    def up_speed2(self):
        return super().up_speed()
    
    def siren(self):
        print("사이렌이 울립니다.")
        
class fire_car(Car):#   상속    
        
    def water(self):
        print("물을 뿌립니다.")
        
a1 = Ambul_car()
print("현재속도: ",a1.speed)    # 0
a1.up_speed()   #   자식(Ambul)의 오버라이딩 된 함수 호출 +20
print("현재속도: ",a1.speed)    # 20
a1.up_speed2()   #   부모(Car)의 함수 호출 +10
print("현재속도: ",a1.speed)    # 30

