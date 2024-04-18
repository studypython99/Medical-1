#   1차원 리스트 생성
a_list = [0]*52
c_list = [i for i in range(52)]
b_list = []
for i in range(52):
    b_list.append(0)
print(a_list)
print(b_list)
print(c_list)

#   2차원 리스트 생성
aa = [[0]*1]*10 #   얕은복사
aa[0][0] = 1    #   전부 바뀐다.
print(aa)
aa[9][0] = 10
print(aa)

bb = [[0]*2 for i in range(10)]

cc = []
for i in range(52):
    dd = []             #   []를 52개 생성
    for i in range(2):  #   0,1 자리에
        dd.append(0)    #   0으로 채운걸 입력한다
    cc.append(dd)       #   [0,0]을 52개 만들어서 입력한다
print(cc)               #   [[0, 0], [0, 0], [0, 0],..52개..[[0, 0]]
