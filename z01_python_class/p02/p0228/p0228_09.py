#   중첩 for
#   for 안에 for
for i in range(3):
    print('안녕')
    for j in range(2):
        print('반가워')

 
# #   for 문을 사용해서 2단을 출력
#   입력받은 숫자의 단을 출력하세요 >>
#   3을 입력받으면 3단 출력, 4를 입력받으면 4단 출력
# n = int(input('단 >>'))

# for i in range(1,10):
#     print('{}x{}={}'.format(n,i,n*i))


#   전체 구구단  
for i in range(2,10):   #   2단~9단까지 출력
    print('[{}단]'.format(i))
    for j in range(1,10):   #   ()x1~9 
        print('{}x{}={}'.format(i,j,i*j),end=' ')   #   i =2, j =1,2,3,4,5,6,7,8,9 1set
    print() #   줄바꿈                                             i =3, j =1,2,3,4,5,6,7,8,9 1set
                                                    #   ..........
                                                    #   i =9, j =1,2,3,4,5,6,7,8,9 1set 99단 완성

#   짝수단 출력
for i in range(2,10):
    if i % 2 == 0 :             #2,3,4,5,6,7,8, 를 다 입력했는데, 2로 나눠서 나머지가 0이 되는 = 짝수
        print('[{}]단'.format(i))
        for j in range(1,10):
            print('{}x{}={}'.format(i,j,i*j),end=' ')
        print()
#   홀수단 출력
for i in range(2,10):
    if i % 2 == 1 :
        print('[{}]단'.format(i))
        for j in range(1,10):
            print('{}x{}={}'.format(i,j,i*j),end=' ')
        print()

#   nx1,3,5,7,9 ??
for i in range(2,10):  
    print('[{}단]'.format(i))
    for j in range(1,10):  
        if j % 2 == 1 :
            print('{}x{}={}'.format(i,j,i*j),end=' ')   
        print() 
    
                                   
#   출력형태
#   1 2 3 4 5                                            
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
# for j in range(5): #    j = 0,1,2,3,4
#     print(j+1,'번째 출력')
#     for i in range(1,6):
#         print(i,end=' ')
#     print()
