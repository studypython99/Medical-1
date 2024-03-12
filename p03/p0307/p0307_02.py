students = {"stNo":1,"stuName":"홍길동","kor":100}
students["eng"] = 100   #   없는 키는 입력, 있는키는 수정
students['kor'] = 50    #   있는 키는 수정
del students["stuName"] #   딕셔너리 삭제
print(students)

#   타입을 list, dict, int, float, str
print(list(students.keys()))    #   딕셔너리 키값 추출  ['stNo', 'kor', 'eng']
print(list(students.values()))    #   value값 추출
print(list(students.items()))    #   ke, value 토플 형태로 추출(토플은 수정, 삭제가 불가능//리스트로 변경시 가능)


# list = [1,2,3]
# list.append(4)
# print(list)
# del list[0]
# print(list)
# list[0] = 100
# print(list)
# list[3] = 1000  #   index 공간을 벗어나면 error, 방이 없는데 추가하려는 상황,,
# print(list)
