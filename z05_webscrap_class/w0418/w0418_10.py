import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5500/stock.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

type_tr = soup.find("tr","type1")#클래스로 찾는방법

print("th: ",type_tr.th)
print("td: ",type_tr.next.next.td)
# print("find_next_sibling: ",type_tr.find_next_siblings())
all = type_tr.find_next_siblings()[1:] #tr요소들
all_tr_list=[]
cnt = 0
for i in all:
    if i.find("td","no"):
    
        tr_list=list(filter(lambda x : x.text.strip() != '', i.find_all('td')))
        tr_list=list(map(lambda x : x.text, tr_list))
        tr_list=list(map(lambda x : x.strip(), tr_list))
        # if cnt ==2:
            # break
        print(i.find_all('td')) #tr요소
        

        all_tr_list.append(tr_list)
    # cnt+=1
print('-'*40)
for i in all_tr_list:
    print(i)
        
    
