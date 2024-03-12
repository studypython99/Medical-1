#   얕은복사 깊은복사
#   변수
a = 1
b = 2
c = a # c에 a의 값을 넣음 >> 위치 동일
print('변수:',a,b,c)
print(id(a))
print(id(c))


a = 8
print('변수:',a,b,c) #다른값을 넣어주게 되면 위치가 달라진다.
print(id(a))
print(id(b))
print(id(c))
#   변수의 값이 변하게 되면 변하는 변수는 다른 메모리 주소로 옮긴다.
#   기존과 메모리 값이 바뀌게 됨을 확인할 수 있다.

#   list는 여러가지 데이터가 들어갈 수 있다.
#   주소 값이 할당된다.
#   단순 복사(cc=aa)는 주소값이 복사된다(=같아진다)
aa = [1]
bb = [2]
cc = aa
print(aa,bb,cc)
print(id(aa)) #2641065267584
print(id(bb)) #2641065269440
print(id(cc)) #2641065267584
aa[0] = 10
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))

#   얕은(단순)복사가 되었기 때문에 aa의 값을 변경하면 cc값이 같이 반영된다.
#   깊은 복사, 독립성 유지
import copy
aa = [1]
bb = [2]
cc = copy.deepcopy(aa)
print(aa,bb,cc)
print(id(aa)) 
print(id(bb)) 
print(id(cc)) 
