class Tv:   #   클래스 선언, 설계도
    channel = 0
    color = "black"
    size = 65
    volume = 0
    
    def up_volume(self,volume):
        self.volume += volume        
    def down_volume(self,volume):
        self.volume -= volume
        
    def up_channel(self,channel):
        self.channel += channel        
    def down_channel(self,channel):
        self.channel -= channel
    

    def __init__(self,channel,color,size,volume):
        self.channel = channel
        self.color = color
        self.size = size
        self.volume = volume
    
#   철수-   화이트, 채널 10, 2증가
tv1 = Tv(10,"화이트",65,2)  #객체선언, 설계도에 따른 제품생산
print("철수:",tv1.channel,tv1.color,tv1.size,tv1.volume)    #변경사항이 없다면 없어도 상관없다.

#   영희-   핑크, 채널 7, 채널 5증가
tv2 = Tv(7,"핑크",65,5)
print("영희:",tv2.channel,tv2.color,tv2.size,tv2.volume)

#   반장-   실버, 채널 1, 채널 3증가
tv3 = Tv(1,"실버",65,3)
tv3.up_channel(3)
print("반장:",tv3.channel,tv3.color,tv3.size,tv3.volume)

    