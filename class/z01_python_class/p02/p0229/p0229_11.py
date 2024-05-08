fruits = ['딸기','사과','자몽','포도','수박','자몽']    #   자몽을 삭제할거야
#   리스트명.remove('요소명')

#   del(리스트명[번호])
del(fruits[-1])
print(fruits)

for i, f in enumerate(fruits):
    print('{}는{}번째에 있습니다.'.format(f,i)) #   f는 i번째에 있습니다.