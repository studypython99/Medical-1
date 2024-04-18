#   stu.txt 파일을 읽어 출력하시오.
students = []   #   전체학생의 리스트
f = open("stu.txt","r",encoding="utf8")
# g = open("stu_dic.txt","w",encoding="utf8")
while True:

    contens = f.readline()  # 한줄씩 stu.txt를 읽어와서
    if contens == "": break
    t_list = contens.split(",") #   csv파일을 , 쉼표로 분리
    s_dic = {
        "stuNo":int(t_list[0]),
        "name":t_list[1],
        "kor":int(t_list[2]),
        "eng":int(t_list[3]),
        "math":int(t_list[4]),
        "total":int(t_list[5]),
        "avg":float(t_list[6]),
        "rank":int(t_list[7]),
    }
    students.append(s_dic)
    # g.write(students) # 이렇게는 저장이 안되나요!?
print(students)
f.close()
# g.close()