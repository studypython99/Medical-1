stu = [
    ["홍일동",10],
    ["홍이동",20],
    ["홍삼동",30],
    ["홍사동",40],
    ["신오동",50],
    ["신육동",60],
    ["신칠동",70],
    ["신팔동",80]
]

#   이름으로 검색, "홍" 이 들어가는 사람을 모두 검색해서 출력하시오
#   이름으로 검색, "신" 이 들어가는 사람을 모두 검색해서 출력하시오
while True:
    print("학생성적검색")
    print("1. 이름 검색")
    print("2. 점수 검색")
    choice = int(input("원하는 번호를 입력하세요 >>"))
    
    
    
    if choice == 1:
        search = input("이름입력 >>")
        #0번에 [0] 1번에[0] 비교하기
        stu_list = []
        cnt = 0
        for i in stu:
            if search in i[0]: #    찾고자하는것 in 범위
                print("찾는 사람이 있습니다 위치: ",cnt)
                stu_list.append(cnt)
            cnt += 1
        print(stu_list)
            #   검색된 사람 출력
            
        print("검색된 사람: ")
        for i in stu_list:
            print(stu[i])
            
    if choice == 2:
        score = int(input("몇점 이상인가요? >>"))
        sco_list = []
        cnt = 0
        for i in stu:
            if i[1] >= score:
                print("찾는 사람의 위치: ",cnt,end=", ")
                sco_list.append(cnt)
            cnt += 1
        #   검색된 사람들 출력
        for i in sco_list:
            print(stu[i])
        print()
