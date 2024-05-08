#   파일 열기
in_file = open("C:\workspace\Medical-1\mem.txt","rb")    #   복사하면 역슬\
out_file = open("C:/a/m1.txt","wb")                     #   슬/ 로 폴더 구분하기

#   파일 읽기, 쓰기
while True:
    bin = in_file.read(1)   #   1바이트씩 읽어온다
    if not bin: break
    out_file.write(bin)
    
#   파일 닫기
in_file.close()
out_file.close()
print("복사가 완료되었습니다.")