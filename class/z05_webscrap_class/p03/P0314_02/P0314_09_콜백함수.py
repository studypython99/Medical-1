#k001.csv 파일에서 전국 인원수를 출력하시오
#   적용년월,시도코드,도시명,사용건수,인원수,사용금액

#   파일열기
f = open("k001.csv","r",encoding="utf8")
#   파일읽기
cnt = 0
sum = 0
while True:
    contens = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if contens == "" : break
    f_list = contens.split(",")
    f_list[-2] = int(f_list[-2])
    sum += f_list[-2]
print(sum)
#   파일닫기
f.close()