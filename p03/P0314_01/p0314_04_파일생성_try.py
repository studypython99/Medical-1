#   파일 1개 생성

#   file open
file = open("memo.txt","w",encoding='utf8')
try:
    #   file write
    file.write("안녕하세요.1\n")
    file.write("안녕하세요.2\n")
    file.write("안녕하세요.3\n")
    print(1/0)
    file.write("안녕하세요.4\n")
except Exception as e:  #   Exception as e 어떤 에러인지 설명해줌.
    print("저장시 에러가 났습니다.")
    print(e)    #   division by zero 나누기 0이다
finally:    
    #   파일 닫기
    file.close()