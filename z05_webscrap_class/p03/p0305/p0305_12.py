import operator #   클래스를 정렬하는 형태

#   딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
         'grapes':'포도','mango':'망고','kiwi':'키위'}

print(t_dic.keys())     #   dict_keys(['peach', 'orange', 'apple', 'pear', 'grapes', 'mango', 'kiwi'])
print(t_dic.values())   #   dict_values(['복숭아', '오렌지', '사과', '배', '포도', '망고', '키위'])
print(t_dic.items())    #   dict_items([('peach', '복숭아'), ('orange', '오렌지'), ('apple', '사과'), ('pear', '배'), ('grapes', '포도'), ('mango', '망고'), ('kiwi', '키위')])    

print(sorted(t_dic.items(),key=operator.itemgetter(0))) #   영어(key)로 정렬
#   [('apple', '사과'), ('grapes', '포도'), ('kiwi', '키위'), ('mango', '망고'), 
# ('orange', '오렌지'), ('peach', '복숭아'), ('pear', '배')]
print(sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True)) #   영어(key)로 역순정렬
#   [('pear', '배'), ('peach', '복숭아'), ('orange', '오렌지'), ('mango', '망고'), 
# ('kiwi', '키위'), ('grapes', '포도'), ('apple', '사과')]
print(sorted(t_dic.items(),key=operator.itemgetter(1))) #   한글(value)로 정렬
#   [('mango', '망고'), ('pear', '배'), ('peach', '복숭아'), ('apple', '사과'), 
# ('orange', '오렌지'), ('kiwi', '키위'), ('grapes', '포도')]








#   3개의 숫자를 입력받아 순서대로 출력하시오.
#   17, 50, 12 > 12, 17, 50
# num1 = [0,0,0]
# for i in range(3):
#     num1[i] = int(input(f'{i+1}번째 숫자를 입력하세요 >>')) #    f"{i+1}"= "{}".format(i+1) 이것과 같음
#     #num1.append(num)
# print(num1)
# num1.sort()
# print(num1)
# print("최대값:",max(*num1))
# print("최소값:",min(num1[0],num1[1],num1[2]))

# a = [5,7,4,8,1,9,3,2]
# a.sort()    #  순차정렬
# print(a)

# b = [5,7,4,8,1,9,3,2]
# b.sort(reverse=True)    #   역순정렬
# print(b)