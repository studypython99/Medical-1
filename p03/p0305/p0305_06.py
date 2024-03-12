import random
a = []
#   1~25까지 숫자를 list에 넣기
for i in range(0,25):
    a.append(i+1)
print(a)
random.shuffle(a)   #   섞어주는 함수 a[0],a[ran] = a[ran],a[0]

#   2차원 리스트에 랜덤으로 섞은 숫자 넣기
arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]    #   미리 만들어두고 입력
for i in range(5):
    for j in range(5):  #  ixj, 5x5의 배열
        #a[i][j] = (5*i)+(j+1)
        arr[i][j] = a[(5*i)+j] #   = (5*i)+(j > 0~24
#print(arr)

#출력
while True:
    print('-'*50)
    print('\t[좌표 맞추기 프로그램]')
    print('-'*50)
    print('순번',0,1,2,3,4,sep='\t')
    print('-'*50)
    for i in range(0,5):
        print(i,end='\t')
        for j in range(0,5):
            print(arr[i][j],end='\t')
        print()
    print('-'*50)
    x = int((input('x좌표를 입력하세요 >>')))
    y = int(input('y좌표를 입력하세요 >>'))
    arr[x][y] = 'X'
    #   세로부터
    
    '''
        [좌표 맞추기 프로그램]
--------------------------------------------------
순번    0       1       2       3       4
--------------------------------------------------
0       13      18      4       16      15
1       20      22      5       6       10
2       19      25      3       2       12
3       11      24      9       8       1
4       14      17      21      23      7
'''
