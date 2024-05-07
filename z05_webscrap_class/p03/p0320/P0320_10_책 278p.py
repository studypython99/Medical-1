def func(n,*val):
    for i in range(n):
        for v in val:
            print(v)
        print()
            
func(5,"안녕","하이","반갑","매개")

#   책 280, 281,

def func(*val,n=2): #키워드매개변수를 넣으려면 맨 뒤로 보낸다 n=2, sep="", end=""
    for i in range(n):
        for v in val:
            print(v)
        print()
            
func("안녕","하이","반갑","매개")

#   316p
#   튜플은 수정삭제가 안된다.

#318p
#a,b의 맞교환

#323p map, filter
