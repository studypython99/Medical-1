#   n1단부터 n2단 까지 출력
n1 = int(input('숫자입력 >>'))
n2 = int(input('숫자입력 >>'))

#   크기비교해서 n1이 더 크면 n2, n1 바꾸기
#   출력 2~4 단 출력
if n1 > n2 :
    n1, n2 = n2, n1         #   
for i in range(n1,n2+1):    #   가로출력
    for j in range(1,10):
        print('{}x{}={}'.format(i,j,i*j),end='\t')
    print()
    
for i in range(1,10):       #   세로출력
    for j in range(n1,n2+1):
        print('{}x{}={}'.format(j,i,i*j),end='\t')
    print()
