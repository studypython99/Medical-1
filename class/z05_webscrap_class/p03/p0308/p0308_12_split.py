#   split() 문자열을 분리시켜준다 ()안의 문자로

hobby = "게임,골프,독서"
print(hobby.split(","))    #   ['게임', '골프', '독서']

h_data = "2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
h_list=h_data.split(",")
#   ['2023-10-23', '1', '강원도 강릉시', '강릉동인병원', '383', '21', '033)651-6167', '강릉대로419번길 42', '종합']
print("병상수: ",h_list[4])
#   csv 파일: ','로 데이터를 구분지어놓은 자료

a_data = "2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split("/")
print("병상수: ",a_list[4])

#   join

ss = "%"
print(ss.join("파이썬"))    #   파%이%썬

s_date = "2023/03/08"   #   연월일을
s_date_list = s_date.split("/") #   /로 구분지어서
print(s_date_list)  #   출력    ['2023', '03', '08']

s_time = "2023:03:08:16:48:00"
s_time_list = s_time.split(":")
print(s_time_list)  #   ['2023', '03', '08', '16', '48', '00']

today = "2024/03/08"
#   10년 후의 날짜를 출력하시오 2034/03/08
today_list = today.split("/")
print(today_list)
today_list[0] = 2034
print(today_list)
today2 = "{}/{}/{}".format(*today_list)
print(today2)