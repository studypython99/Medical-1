#   가변매개변수, values

def str_title(num,*txt):    #   num은 받고, 뒤에는 묶어서 다 받아주겠다. 리스트 타입으로 받겠다.
    print("txt type: ",type(txt))
    print(txt)
    for i in range(num):
        for t in txt:
            print(t,end=" ")
        print()
'''
txt type:  <class 'tuple'>
('안녕', '잘가', '안녕하세요', '반갑습니다')
안녕 잘가 안녕하세요 반갑습니다
'''            
        
str_title(1,"안녕","잘가","안녕하세요","반갑습니다")