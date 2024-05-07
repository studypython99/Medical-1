import os


# if not os.path.exists("hello"): #   폴더가 존재하지 않는다면
#     os.mkdir("hello")             #   생성
# else:
#     os.rmdir("hello")             #   삭제
    
    
# #   1. 파일생성    
f = open("students.txt","w",encoding='UTF8')   
f.write("1,'홍길동',100,99,87,286,95.33,2\n") 
f.write("2,'유관순',98,93,87,278,92.67,3") 
f.close()   #   닫기

# #   2. 파일생성, with 사용하면 f.close() 없이도 가능
# with open ("students11.txt","w") as f:
#     f.write("1,'홍길동',100,99,87,286,95.33,2")

#   파일 읽어오기
t_list = []
out_f = open("students.txt","rt",encoding='UTF8')   #   UTF-8: 국제규격 한글인코딩값 / EUC-KR: 한국에서의 규약
while True:
    txt = out_f.readline()# 1줄씩 읽어오기
    if txt == "":   #   다 읽었으면 break.
        break
    print(txt)
out_f.close()    #  파일 닫기
str1 = "1,'홍길동',100,99,87,286,95.33,2"
s_list = str1.split(",")    #   파일변환하기
for i in s_list:
    print(i)
    
#   파일삭제
os.remove("students.txt")