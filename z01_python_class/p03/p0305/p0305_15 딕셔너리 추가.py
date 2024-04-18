import operator
fruits = ['바나나','딸기','배','바나나','바나나','딸기',
           '배','바나나','배','사과','배','바나나','배','사과','딸기']
counter = {}
for f in fruits:
    if f not in counter:
        counter[f] = 0  #   비어있는 카운터 딕셔너리에, key를 추가시킴
    counter[f] += 1     #   key에 해당되면 1씩 추가
    
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))   
#   counter.items() >> 튜플 형태로 나오게 한다