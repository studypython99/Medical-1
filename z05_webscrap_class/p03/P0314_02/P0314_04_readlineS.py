#   파일 읽어오기
#   1. 파일 열기
#   2. 파일 읽기 read*()
#   read(): 모든 문자열을 가져옴.
#   readline(): 한줄씩 가져옴.
#   learlines(): 한줄씩 리스트 타입에 입력해서 모두 가져옴.
#   3. 파일 닫기

#   파일 유무 확인
import os
if os.path.exists("str.txt"):   #   파일 유무 확인.

    with open("str.txt","r",encoding="utf8") as f: #    as f = f 라는 별칭으로 부르겠다
        txt_list = f.readlines()
        for txt in txt_list:
            print(txt,end="")
        print()
else:
    print("파일이 없습니다.")
    '''
안녕하세요. 반갑습니다.
저는 홍길동 입니다.
파이썬 수업을 열심히 듣고 있습니다.
'''
    # with 사용시 f.close() 생략가능


# #   readlines
# f = open("str.txt","r",encoding="utf8")
# txt_list = f.readlines()
# f.close()

# print(txt_list)     #   한줄씩 리스트 타입으로 저장해서 가져온다. 
#   ['안녕하세요. 반갑습니다.\n', '저는 홍길동 입니다.\n', '파이썬 수업을 열심히 듣고 있습니다.\n']

# #   read line #   한줄을 str타입으로 가져옴.
# f = open("str.txt","r",encoding="utf8")
# while True:
#     txt =f.readline()
#     if txt == "": break
    
#     print(txt,end="")
