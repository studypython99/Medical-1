import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
####################################################################################
#찾고싶은 자료의 가장 가까운 상위요소 확인
#
type1_tr = soup.find("tr","type1")
print(type1_tr.text) #첫번째 <tr><th> ~ </th></tr>까지: 순위,종목~
print('-'*40)
print(type1_tr.th.text) # tr>th*1 첫번째 th: 순위
print('-'*80)
# print(type_tr.find_next_siblings())
trs = type1_tr.find_next_siblings()#tr의 다음next, 형제들siblings
print('-'*40)
for tr in trs:
    if tr.find("td","no"): # 만약, tr 종목 한줄한줄마다, td 클래스 no가 있다면
        tr.find_all('td')# tr에서 td 전체를 찾아오고,
        print("tds : ", tr.find_all('td')) #td요소
        print('-'*40)
    
#모든 td를 찾




# type_tr = soup.find("tr","type1")#클래스로 찾는방법

# print("th: ",type_tr.th)
# print("td: ",type_tr.next.next.td)
# print('-'*40)
# print("find_next_sibling: ",type_tr.find_next_siblings())
# # all = type_tr.find_next_siblings()[1:] #tr요소들
# all_tr_list=[]
# cnt = 0
# for i in all:
#     if i.find("td","no"):
#         # filter: 조건을 만족하는 경우에만 가져온다, map: 각 요소마다 적용 >>>모두 list로 감싸준다
#         tr_list=list(filter(lambda x : x.text.strip() != '', i.find_all('td'))) #텍스트가 없다면 가져오지 않겠다. 리스트의 요소 하나하나 적용시킴
#         tr_list=list(map(lambda x : x.text, tr_list))# 텍스트만 추출
#         tr_list=list(map(lambda x : x.strip(), tr_list))# 추출한 데이터의 공백을 제거
#         # if cnt ==2:
#             # break
#         print(i.find_all('td')) #tr요소
        

#         all_tr_list.append(tr_list)
#     # cnt+=1
# print('-'*40)
# for i in all_tr_list:
#     print(i)
#     """
#     출력결과
# ['1', '삼성전자', '4.28%', '79,600', '700', '+0.89%', '19,789,459', '78,800', '80,100', '78,300', '37.35', '4.15']
# ['2', 'HLB', '1.82%', '97,300', '4,100', '+4.40%', '1,462,315', '92,900', '98,500', '91,600', '-66.24', '-32.55']
# ['3', '삼성중공업', '1.52%', '9,540', '850', '+9.78%', '38,822,652', '8,800', '9,710', '8,800', '-56.79', '-4.22']
#     """
        
    
