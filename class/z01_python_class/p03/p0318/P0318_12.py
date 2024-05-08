#   Car 클래스를 선언해서 
class Car:
#   carCount 클래스 변수
    carCount = 1    #   1부터 입력한다 
#   carNo에는 carCount 숫자를 이용해서 carNo를 넣으시오.
    carNo = 0   #   처음엔 carCount(1)+carNo(0), 두번째엔 ...?
#   carNo 클래스 변수를 이용해서 숫자를 증가
#   color="white", door=5, tire=4, speed
    def __init__(self,color="white",door=5,tire=4,speed=0):
        self.carNo = Car.carCount
        
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1
        
    def up_spd(self):
        self.speed += 10
        
    def down_spd(self,speed):
        self.speed -= speed-10

#   up_speed 함수를 호출하면 +10씩 증가
#   down_speed 함수를 호출하면 -10씩 감소

#   c1: white,5,4,0 >>speed 30
c1 = Car("white",5,4,0)
for i in range(3):
    c1.up_spd()
    print(i, c1.speed)  #   i 찍고, 보고싶은거 c1.speed 찍고
#   c2: red,5,4,0 >>speed 100
c2 = Car("red",5,4,0)
for i in range(10):
    c2.up_spd()
#   c3: silver,5,4,0 >>speed 70
c3 = Car("silver",5,4,0)
for i in range(7):
    c3.up_spd()
#   car_list 추가하고
car_list = []
car_list.append(c1)
car_list.append(c2)
car_list.append(c3)
#   car_list 모두(color,door,tire,speed) 출력하세요.
for i in range(len(car_list)):    
    print(car_list[i].carNo,car_list[i].color,car_list[i].door,car_list[i].tire,car_list[i].speed)

