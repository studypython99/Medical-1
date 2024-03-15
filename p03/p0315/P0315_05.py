while True:
    print("-"*40)
    print("[회원정보]")
    print("-"*40)
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 회원정보수정")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요 >>"))
#-----------------------------------------------------            
    if choice == 1:
        print("1. 회원가입")
        c_id = input("새로운 id를 입력하세요 >>")
        c_pw = input("새로운 pw를 입력하세요 >>")
        f = open("mem.txt","a",encoding="utf8")
        f.write(f"{c_id},{c_pw}\n")
        f.close()
        print(f"id:{c_id}, pw:{c_pw}로 회원가입 되었습니다.")
#-----------------------------------------------------            
    elif choice == 2:
        print("2. 로그인")
        c_id = input("ID를 입력하세요.>> ")
        c_pw = input("PASSWORD를 입력하세요.(0.종료)>> ")
        if c_pw == "0": break # 0.종료
        #   mem.txt로 로그인을 구현
        f = open("mem.txt","r",encoding="utf8")
        m = []
        suc_flag = 0
        while True:
            txt = f.readline()
            if txt == "" : break
            m = txt.split(",")  # , 로 구분지어서 가져온다
            m[0] = m[0].strip() #   여백제거
            m[1] = m[1].strip()
            if c_id == m[0] and c_pw == m[1]:
                suc_flag = 1    # idpw 맞으면 while문 종료
                break
        f.close()
        if suc_flag ==1:
            print("로그인 성공")
        else:
            print("아이디 또는 패스워드가 일치하지 않습니다.")
#-----------------------------------------------------            
    elif choice == 3:
        #   파일에 있는 모든 정보를 리스트에 저장한다.
        member = []
        f = open("mem.txt","r",encoding="utf8")
        while True: #   회원정보를 member리스트에 저장
            txt = f.readline()
            if txt == "": break
            t_list = txt.split(",")
            t_list[0] = t_list[0].strip()
            t_list[1] = t_list[1].strip()
            member.append([t_list[0],t_list[1]])
        print("3. 회원정보수정")
        search = input("ID를 입력하세요.>> ")
        cnt = 0
        for m in member:
            if search == m[0]:  #   동일 id 확인
                break
            cnt += 1
            
        if cnt == len(member):
            print("없는 id 입니다. 다시 입력하세요.")
        else:
            print("pw 수정")
            pw_input = input("수정 할 pw 입력 >>")
            member[cnt][1] = pw_input   #   member리스트에서 수정 완
            #   member리스트를 다시 저장.
            f =open("mem.txt","w",encoding="utf8")
            for m in member:
                f.write(f"{m[0]},{m[1]}\n")
        
        
        f.close()
        