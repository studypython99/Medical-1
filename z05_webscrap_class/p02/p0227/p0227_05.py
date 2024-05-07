#   0~20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
#   출력: [0,5,10,15,20]
#   for, append 
num = []
for i in range(21):
    if i % 5 == 0 :
        #print(i,end=',')
        num.append(i)
#        print(num)
    else:
        pass
print(num)
print()   

lan = ['c','python','java','jquery','css']
#   1. 하나하나 출력해보기 for
for i in range(len(lan)):
    print(lan[i],end=',')
#   2.  1.c
#       2. python
#       3. java
#       4. jquery
#       5. css  이렇게 출력해보기 for i 사용
print()
for i in range(len(lan)):           # i는 0부터 시작한다.
    print(str(i+1)+'.',lan[i])    # 문자, 숫자를 변경해서 , +를 변경 가능, +는 str에서 사용가능.

num = [1,-1,2,3,-4,5,6,-8,9,-10]
#   양수면 [양수], 음수면 [음수] 출력 for 사용
for i in range(len(num)):
    if num[i] > 0 :
        print('{}: 양수'.format(num[i]),end=', ')
        #print(num[i],'양수',end=', ')
    else:
        print('{}: 음수'.format(num[i]),end=', ')
        #print(num[i],'음수',end=', ')
        
print()
for n in num:
    print(n, end=':')   # 1:양수    이런식으로 표현됨
    if n >= 0 :
        print('양수')
    else:
        print('음수')