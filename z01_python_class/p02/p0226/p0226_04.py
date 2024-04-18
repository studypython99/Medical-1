#   quizz
stu = ['홍길동','유관순','이순신','김구','강감찬']

#   1. 이순신학생출력   index
print(stu[2])
#   2. 김구 이름을 안창호로 변경    index
stu[3]='안창호'
print(stu)
#   3. 유관순부터 강감찬 출력   slicing
print(stu[1:])
print(stu[1:5]) #   5 대신 4+1도 가능
#   4. 왕건을 추가  append
stu.append('왕건')
print(stu)
#   5. 홍길동 삭제  remove, del
del stu[0] #    요소의 위치를 삭제
#   stu.remove('홍길동') > 값을 삭제
print(stu)

f = ['사과','복숭아','딸기','배','포도','수박']
#   딸기출력
print(f[2])
#   포도를 망고로 바꾸기
f[4] = '망고'
print(f)
#   배부터 끝까지 출력
print(f[3:])
#   복숭아 딸기 출력
print(f[1:3])
#   사과 추가
f.append('사과')
print(f)
#   감 추가
f.append('감')
print(f)
#   사과 삭제
f.remove('사과')
print(f)
#   수박이 있으면 [수박이 있습니다] 출력
if '수박' in f :
    print('수박이 있습니다')
else:
    print("수박이 없습니다")
    
num = [10,20,30,40,50]
#   60이 없으면 60 추가
if 60 not in num :
    num.append(60)
    print(num)
else:
    print(num)
#   20이 있으면 70 추가하고 20 삭제
if 20 in num :
    num.append(70)
    num.remove(20)
    print(num)
else:
    print(num)
    
aa = [[1,2],[3,4]]
print(aa[0][1]) #   2
print(aa[1][1]) #   4
a1 = [1,2]
a2 = [3,4]
a3 = [a1,a2]    #   a3 = aa

stu1 = ['홍길동',90]
stu2 = ['유관순',100]
student = [stu1, stu2]
#   student리스트를 사용해서 유관순 출력
print(student[1][0])
#   student리스트를 사용해서 홍길동 점수를 80으로 수정     
student[0][1] = 80 #    list형은 [] 로 작성해야한다 ()x
print(student[0][1])
#   이순신 95점을 student에 추가
stu3 = ('이순신',95)
student.append(stu3)
print(student)