import operator

foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치",
         "피자":"피클","맥주":"땅콩","삼겹살":"상추"}

#   키의 값을 출력하시오.
print(foods.keys())
for key in foods:
    print(key,end="\t")
#   value의 값을 출력하시오
print(foods.keys())
for value in foods:
    print(foods[value],end="\t")
#   key:value 형태로 모두 출력하시오.
print(foods)
for kv in foods:
    print(f"{kv}:{foods[kv]}")

print(sorted(foods.items(),key=operator.itemgetter(0))) #   key >>>
print(sorted(foods.items(),key=operator.itemgetter(0),reverse=True)) #   reverse, key >>>
print(sorted(foods.items(),key=operator.itemgetter(1))) #   value >>>