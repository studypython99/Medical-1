#   학번 1000, 이름 홍길동, 학과 컴퓨터공학
student = {"학번":1000,"이름":"홍길동","학과":"컴퓨터공학"}

for key in student:   # 키 값이 넘어온다
    print("key: ",key)
    
#   연락처 010-1111-1111
student["연락처"] = "010-1111-1111"
print(student)

#   수정하기
student["이름"] = "유관순"
print(student)

#   학과 > 화학과 변경
student["학과"] = "화학과"
print(student)


print(student["이름"])      #   key의 value값 출력
print(student.get("이름"))

# print(student["성별"])  #   key값이 없을 때 error
# print(student.get("성별")  #   error는 없고 none 라고 표시됨 (얻어볼까? 없어요~)

if "이름" in student:
    print("이름 키값이 있습니다.")
    print(student["이름"])
else:
    print("이름 키값이 없습니다.")
if "성별" in student:
    print("성별 키값이 있습니다.")
    print(student["성별"])  # error 프로그램이 멈춘다.
else:
    print("성별 키값이 없습니다.")
    
#   student.keys() 딕셔너리의 모든 키값을 반환한다
print(type(student.keys()))   #   <class 'dict_keys'> 리스트타입으로 출력된다.

list(student.keys())    #   형태 변환을 해야 완전한 리스트형이 된다.

for i in student.keys():
    print(i)

#   student.value()     딕셔너리의 모든 value를 출력
print(student.values())         #   class type. 
print(list(student.values()))   #   list type
for i in student.values():
    print(i)
    
#   items() 튜플 형태 데이터를 리턴
print(student.items())  #   데이터(값)의 삭제, 수정 안됨
#   dict_items([('학번', 1000), ('이름', '유관순'), ('학과', '화학과'), ('연락처', '010-1111-1111')])

if '이름' in student:   #   T or F 형태로 확인 가능, 있으면 출력하고 없으면 출력하지마
    print('키값이 있습니다.')
else:
    print('키값이 없습니다.')