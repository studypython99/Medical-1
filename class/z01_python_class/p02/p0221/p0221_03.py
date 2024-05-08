#   format을 사용
print("%d-%5d-%05d"%(123,123,123))
print("{0:d}-{1:5d}-{2:05d}".format(123,123,123))
print("{}-{}-{}".format(123,123,123))
print("{}-{}-{}".format(1,3.14,"안녕"))

print("{}+{}={}".format(1,2,1+2))

print("{} {}".format(1,2,3)) #뒤에 숫자가 많은건 ok
#print("{} {} {}".format(1,2)) # 부족하면 안됨;;

#강제 행나누기, 띄어쓰기
print("오늘은 날씨가 흐림. 내일은 날씨가 맑음")
# \n : 행나누기
print("오늘은 날씨가 흐림.\n내일은 날씨가 맑음")
# \t : 띄어쓰기 Tab 만큼 띄어쓰기됨
print("오늘은 날씨가 흐림.\t내일은 날씨가 맑음")

# 따옴표를 사용하는 방법 ", ' 구분해서 사용하기
# \" 사용해서 " 만으로도 사용 가능
print("철수가 말했습니다. '영희의 생각은 어떨까?'")
print('철수가 말했습니다. "영희의 생각은 어떨까?"')
print("철수가 말했습니다. \"영희의 생각은 어떨까?\"")

# \ 출력하기
print("\\n은 줄바꿈입니다.")

print("""\
안녕하세요.
반갑습니다\
    """)