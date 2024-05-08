#   medical_1.csv 파일을 읽어와서 출력하시오.

#   파일열기
f = open("medical_1.csv","r",encoding="utf8")   #오류시, 파일 인코딩값 확인
#   파일읽기
cnt = 0 #   0번줄, 자료의 제목/구분 등 제거하기위함
sum = 0
while True:
    contens = f.readline()
    if cnt == 0:    #   0번줄은 지나가서
        cnt += 1    #   1번줄부터 볼게,
        continue
    if contens == "": break
    f_list = contens.split(",")
    f_list[1] = int(f_list[1])  #   [1] 각 줄의 1번째 방
    sum += f_list[1]
print(sum)
    # for i in f_list:
    #     print()
        
        
#   파일닫기
f.close()