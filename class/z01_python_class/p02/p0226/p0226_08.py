#   반복문
#   안녕하세요 다섯번 출력
print('안녕하세요'*5)

'''
for 변수 in 반복가능한데이터:
    수행할 문장
'''
#   순차적으로 커질 때 range를 사용한다.
for i in range(0,5,1): #    range(시작값, 끝값+1, 증가값), i 가 0,1,2,3,4
    print('안녕')
for i in range(0,5,1): #    range(시작값, 끝값+1, 증가값), i 가 0,1,2,3,4
    print(i,'안녕')
for i in range(0,5): #    증가값이 1인 경우 생략 가능 (0부터, 5회)
    print(i,'hi')
for i in range(2): #    n번 반복할 경우 range(n)
    print(i,'hi there')
for _ in range(2): #    i를 사용하지 않고 _ 사용 가능
    print('hi there')
    
for i in range(5):  #   5번을 반복하시오.
    # num = int(input('숫자를 입력하세요 >>'))
    # print('입력한 숫자는:{}'.format(num))
    
#   i, j 카운터 변수, k, l .. i, j를 자주 사용
#   카운터변수는 반복 샐행 될때마다 현재 실행 횟수에 해당하는 숫자가 들어감.
#   가장 처음은 실행한적이 없으므로 0이 된다.

    for i in range(3): #   증가값이 1인 경우 생략
        print(i)    #   0,1,2 순차적 출력
    
str1 = '안녕하세요'
for i in str1:
    print(i)
    
#   1. 1에서부터 15까지 출력해보세요
for i in range(1,16):
    print(i)
#   2. 10을 4번 반복해서 출력해보세요
for i in range(4):
    print(10)
#   3. helloworld를 6번 반복해서 출력해보세요
for i in range(6):
    print('helloworld')
#   4. 1-100 사이의 2의 배수를 출력해보세요
for i in range(2,100,2):
    print(i)    #   print(i, end='') print(i, end=', ')
    print(i, end=', ')