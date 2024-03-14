#   stu.txt파일을 출력하시오
file = open("stu.txt","r",encoding="utf8")
txt = file.readline()
#   if txt == "": break
t_list = txt.split(",")
t_list[0] = int(t_list[0].strip())
t_list[1] = t_list[1].strip()
t_list[2] = int(t_list[2].strip())
t_list[3] = int(t_list[3].strip())
t_list[4] = int(t_list[4].strip())
t_list[5] = int(t_list[5].strip())
t_list[6] = float(t_list[6].strip())

print(t_list)

file.close()

for i in t_list:
    print(i)


# #   파일 읽어오기

# file = open("str.txt","r",encoding="utf8")
# while True:
#     txt = file.readline()   #   파일 1줄 읽어오기
#     if txt == "":
#         break
#     print(txt,end="")

# file.close()


# #   파일저장
# file = open("str.txt","w",encoding="utf8")

# file. write("안녕하세요. 반갑습니다.\n")
# file. write("저는 홍길동 입니다.\n")
# file. write("파이썬 수업을 열심히 듣고 있습니다.\n")

# file.close()
# print("파일이 저장되었습니다.")