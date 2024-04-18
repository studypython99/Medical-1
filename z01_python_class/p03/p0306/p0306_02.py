import operator
fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}
'''
딕셔너리로 저장하면, 형태소분석이 쉽다
'''

for f in fruit:
    if f not in counter:    #   딕셔너리에 키가 존재하는지 확인    
        counter[f] = 0      #   딕셔너리에 키가 없을 때 키 추가
    counter[f] += 1         #   키의 value값 1 증가
print(counter)

print(sorted(counter.items(),key=operator.itemgetter(0)))
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
#     정렬을/ 튜플형태로 전환/ 키값을 받아온다/ 0번째(key)로/   +@역순정렬/
print(sorted(counter.items(),key=operator.itemgetter(1)))
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))
#                                          1번째(value)로/   +@역순정렬/