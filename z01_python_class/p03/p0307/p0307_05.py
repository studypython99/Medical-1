words = [{},
        {"airplane":"비행기","bank":"은행","bean":"콩",            
        "apple":"사과","bakery":"빵집","banana":"바나나",},
        
        {"run" : "달리다","walk" : "걷다",
        "sit" : "앉다","stand" : "서다",
        "sleep" : "자다","read" : "읽다",
        "look" : "보다","do" : "하다",
        "feel" : "느끼다","go" : "가다"},
        
        {"accumulated":"누적된","additional":"추가적인",
        "adequate":"적당한","administrative":"관리의",
        "affordable":"알맞은","alternative":"대체 가능한",
        "annual":"해마다의","different":"다른",
        "local":"지역의","social":"사회의",}
        ]
w_noun = {}
w_verb = {}
w_ad = {}
w_title = [" ","명사","동사","형용사"]
#         0    1      2     3
        # print("명사를 선택하셨습니다.")
        # choice = input("시작합니다 (1.실행 0.취소) >>")
        # if choice == "1":

while True:
    print("[영단어 맞추기 프로그램]")
    print("1. 명사")
    print("2. 동사")
    print("3. 형용사")
    print("0. 종료")        
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요 >>"))
    right = 0
    wrong = 0
    if choice == 1:
        print("{}를 선택하셨습니다.".format(w_title(choice)))
        chk = input("시작합니다 (1.실행 0.취소) >>")
        if chk == "1":
            for key in w_noun:
                answer = input("{} 단어의 뜻은?".format(key))
                if answer == words[choice][key]:
                    print("정답입니다.")
                    right += 1
                else:
                    print("틀렸습니다. 정답: {}".format(words[choice][key]))
                    wrong += 1
                # print(key,":",w_noun[key])
            print(f'{right}개 맞았습니다.')
            print(f'{wrong}개 틀렸습니다.') # 오답갯수=전체문제-정답
            print("메뉴로 돌아갑니다.")
        
        
    elif choice == 2:
        print("동사를 선택하셨습니다.")
        pass
    elif choice == 3:
        print("형용를 선택하셨습니다.")
        pass
    else:
        print("프로그램을 종료합니다.")
        break