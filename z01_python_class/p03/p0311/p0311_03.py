#   구구단
#   변수가 있어야 한다.
temp = 0
for i in range(1,10):
    # if i == 2: break
    for j in range(1,10):
        if j == 5:
            temp = 1
            break
        print(f"{i}x{j}={i*j}")
    if temp == 1: break     #   이걸 이용해서 전체종료도 가능하다 -1 이면 종료; 뭘까?
    
# 1x1=1
# 1x2=2
# 1x3=3
# 1x4=4