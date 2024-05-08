while True:
    print("[로그인]")
    id = input("아이디: ")
    pw = input("패스워드: ")
    
    
    #파일에서 아이디와 패스워드 확인
    with open("member.csv","r",encoding="utf8") as f:
        while True:
            txt = f.readline()
            if txt == "": break
            mem = txt.split(",")
            #아이디, 패스워드 비교
            if id == mem[1] and pw == mem[2]:
                chk = 1
                break
            
    #id,pw가 없으면 chk==0 , id,pw가 있으면 chk==1
    
    
    if chk == 1:
        print("로그인 되었습니다.")
        break