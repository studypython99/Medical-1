# str.txt 파일의 내용을 모두 출력하시오.

#   str.txt 파일 내용을 읽어와서
#   str1.txt 파일에 그 내용을 추가해보세요.

#   파일열기, 일단 전부 '다' 열어
f = open("str.txt","r",encoding="utf8") 
g = open("str1.txt","a",encoding="utf8")
h = open("str2.txt","w",encoding="utf8")

#   파일 읽기 및 추가
while True:
    contens = f.readline()
    if contens.strip() == "": # 빈공간 제거
        break #   더이상 읽을게 없으면 break
    print(contens,end="")
    g.write(contens+"\n")
    h.write(contens+"\n")

#   파일 닫기, 일 끝나면 '다' 닫아
f.close()
g.close()   
h.close()