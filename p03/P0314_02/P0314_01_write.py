#   파일열기
file = open('memo.txt','w',encoding="utf8")

#   파일쓰기
# for i in range(10):
#     file.write(f"안녕하세요.{i+1}\n")



print("[학생성적입력]")
print("-"*40)
while True:
    txt = input()
    if txt == "0":
        print("학생성적을 저장합니다.")
        break
    print(txt)
    file.write(txt+'\n')