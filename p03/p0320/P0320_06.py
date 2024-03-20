#   input으로 입력받은 데이터를
# p_0320.txt 파일을 생성해서 저장하시오.
#   p_0320은 현재날짜를 사용하시오

import datetime
now = datetime.datetime.now()
print(now.year)
write_input = input("메모를 입력하세요 >>")
f = open(f"p_0{now.month}{now.day}","w",encoding="utf8")
f.write(write_input)
f.close()

