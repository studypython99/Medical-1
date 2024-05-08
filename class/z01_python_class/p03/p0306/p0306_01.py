import operator
fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}
#   딕셔너리 추가
counter["복숭아"] = 4
counter["바나나"] = 4   #   딕셔너리 추가
del counter['복숭아']   #   딕셔너리 삭제
print(counter)
print("keys:",counter.keys())
print("values:",counter.values())
print("items:",counter.items())
# counter["바나나"] = 1   #   딕셔너리 수정
# print(counter["딸기"])  #   딕셔너리에 없는 키값을 출력시 error, 키값이 존재하는지 확인한다 !!
# if "딸기" in counter:     #   질문을 먼저 해서
    # counter["딸기"] = 0     #   입력해 주어야 한다, 키값을 만든다
# else:
#   print(counter["딸기"])  #   키의 value값을 출력
'''
변수: 1개 값 저장
리스트: 복수 저장   []
딕셔너리: 복수 저장(key : value) {}
생성, 추가, 삭제, 수정하는 각각의 방법
data 몇개를 얼마나 저장해야하나?

'''

