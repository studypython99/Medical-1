#   재귀함수, 자기 자신을 다시 부르는 함수
def count(num):
    if num >= 1:
        print(num,end=' ')
        count(num-1)    #   함수를 다시 호출
    else:
        return  #   num < 1 
    
count(10)
print()

for i in range(10,0,-1):
    print(i,end=', ')
print()