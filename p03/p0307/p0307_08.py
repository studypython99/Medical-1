import random

fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
         'grapes':'포도','mango':'망고','kiwi':'키위'}
fruit['peach']      # =복숭아
fruit['kiwi']       # =키위
f_list = list(fruit.keys())     #   dict > list 형태로 바꿔준다
print(f_list)   #   ['peach', 'orange', 'apple', 'pear', 'grapes', 'mango', 'kiwi']

f_list_ran = random.sample(f_list,4)
print("랜덤추출: ",end=',')


