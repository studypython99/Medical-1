#   이름 한글자라도 포함되어 있다면 검색하는 방법
#   찾은사람의 위치 저장
name = ["홍길동","유관순","이순신","김구","강감찬","홍길순","홍길자"]

while True:
    
    search = input("이름을 입력하세요 >>")
    search_list = []
    cnt = 0
    for n in name:
        if n.find(search) != -1: #   -1은 없다, !=아니다, 없는건 아니다??
            print("찾는 사람이 있습니다. 위치: ",cnt)
            search_list.append(cnt)
        cnt += 1
    #   검색된 사람들 출력
    if len(search_list) == 0: print("찾는 사람이 없습니다.")
    else:
        print(f"{search} 검색된 사람 :",end=", ")
        for i in search_list:
            print(name[i],end="")
        print()


# 정확한 이름으로 찾는 방법
  
# # name = ["홍길동","유관순","이순신","김구","강감찬","홍길순","홍길자"]

# search = input("이름을 입력하세요 >>")
# cnt = 0
# for n in name:
#     if search == n:
#         print("찾는 사람이 있습니다. 위치: ",cnt)
#         break
#     cnt += 1
# if cnt == len(name):
#     print("{} 없습니다.".format(search))