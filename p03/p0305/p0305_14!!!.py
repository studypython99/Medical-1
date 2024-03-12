import operator
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}    #   같은숫자가 몇번 나왔는가    {'1': 2번, '2': 1번}
# counter["1"] = 2
# counter["2"] = 1
print(counter)
for number in numbers:          #   없을땐 공간을 만들고 // 있을땐 1씩 추가 잘모르면 파이썬튜터 해보기
    if number not in counter:   #counter딕셔너리에 키값이 없으면
        counter[number] = 0     #키값을 딕셔너리에 추가
    counter[number] += 1        #   딕셔너리에 1씩 추가
    # counter[number] = 0     #   {1: 0, 2: 0, 4: 0, 6: 0, 3: 0, 7: 0}
    
#   많이 나온 숫자로 정렬(오름차순)
#   print(sorted(foods.items(),key=operator.itemgetter(1))) #   value >>>
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))               #   key, 내림차순
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))  #   value, 오름차순
#출력   정렬    자료를          정리할건데 0=key 1=value reverse=True >> 역순    
        