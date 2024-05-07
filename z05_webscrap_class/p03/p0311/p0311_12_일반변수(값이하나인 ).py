def stu_update(stuNo,name,kor,eng,math):    #   지역변수
    stuNo = 2
    name = "유관순"
    total = kor+eng+math
    avg = total/3
    return stuNo, name, total, avg,     #   리턴의 순서와


#   값이 하나만 들어가는 변수
stuNo = 1
name = "홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0

#   함수호출
stuNo, name, total, avg = stu_update(stuNo,name,kor,eng,math) #   전역변수,  6번줄 리턴을 받는 순서도 중요하다


print("학생1: ",stuNo,name,kor,eng,math,total,avg)  #   학생1:  1 홍길동 100 100 100 300 100.0