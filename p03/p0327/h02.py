
    
    #파일열기
    #상대경로, 현재 폴더 안에서 찾아오겠다.
    #medical 폴더 안 member.csv
    #절대경로
    #C:\workspace\Medical-1\p03\p0327\member.csv
with open("C:\workspace\Medical-1\p03\p0327\member.csv","r",encoding="utf8") as f:
    while True:
        txt = f.readline()
        if txt == "": break
        mem = txt.split(",")
        #아이디, 패스워드 비교
        print(mem[0],mem[1])
