import operator

fruits = ["apple","banana","kiwi","pear","peach",
          "apple","apple","kiwi","kiwi","peach","peach",
          "apple","apple","apple","pear","pear","pear",
          "peach","banana","banana",
          ]

counter = {}

for f in fruits:
  if f not in counter:
    counter[f] = 0
  counter[f] += 1
print(counter)
print(sorted(counter.items()))  
# [('apple', 6), ('banana', 3), ('kiwi', 3), ('peach', 4), ('pear', 4)]
print(sorted(counter.items(),key=operator.itemgetter(0)))
# [('apple', 6), ('banana', 3), ('kiwi', 3), ('peach', 4), ('pear', 4)]
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))  # 역배열
# [('pear', 4), ('peach', 4), ('kiwi', 3), ('banana', 3), ('apple', 6)]

# numbers = [1,2,3,4,5,5,6,7,4,3,2,12,67,8,9]

# counter = {}

# for n in numbers:
#   if n not in counter:
#     counter[n] = 0
#   counter[n] += 1

# print(counter)