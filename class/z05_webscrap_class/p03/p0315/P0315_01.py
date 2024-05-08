#   로그인


temp = 0
while True:
    if temp == 1:   break #   어디서든 temp로 프로그램 종료
    print("[학생성적 프로그램]")
    print("-"*40)
    print("*로그인을 해주세요")
    print()
    c_id = input("iD를 입력하세요 >>")
    c_pw = input("pW를 입력하세요(0. 종료) >>")
    
    if c_pw == "0": break   #   로그인 종료
    
    #   로그인 확인
    #   for문으로 비교
    success_flag = 0    # 실패 시,
    for m in member:
        if c_id and c_pw in m:  # c_id == m[0] and c_pw == m[1]
            success_flag = 1  #   로그인 확인
            print("로그인 되었습니다.")
            break   #   맞았으면 끝냅시다.
        else:
            print("다시 입력하세요.")
            #   이 이후에 학생성적프로그램 시작
        print()
        while True:
            print("-"*40)
            print("[학생성적프로그램]")
            print("-"*40)
            print("1. 학생성적데이터 읽어오기")
            print("2. 학생성적입력")
            print("3. 학생성적출력")
            print("0. 프로그램 종료")
            print("-"*40)
            print()
            choice = int(input("원하는 번호를 입력하세요 >>"))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 0: temp = 1  #   프로그램 완전종료
                
            
            
    else:   #   로그인 실패
        print("iD 또는 pW가 일치하지 않습니다. 다시 입력하세요.")
        print()
        
print("프로그램을 종료합니다.")