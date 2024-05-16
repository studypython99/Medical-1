import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
df

# df = pd.read_excel('20122022_출생.xlsx',skiprows=2,nrows=3, usecols='B:M',index_col=0)
# df.index.name = '제목'
# df.index

# 문자열 함수
# slice : 문자열 자르기
# df_str['idx'].str.slice(1,3)
# # df_str['idx'].map(lambda x:x[1:3])  #map(함수) , lambda : 익명함수

# # split : 문자열 분리
# a_list = ['데이터,분석가','영희,철수,바둑이','국어,영어,수학,과학,사회']
# data = {"d_split":a_list}
# df_str = pd.DataFrame(data)
# s_data = df_str['d_split'].str.split(',') #배열로 분리되어 리턴
# s_data

# json데이터 변경
json_data = res.json()
json_data
df = pd.DataFrame(json_data['data'])
df

### 오라클 연결, 데이터를 pandas변환
import oracledb
import pandas as pd
conn = oracledb.connect(user='ora_user2',password='1111',dsn='localhost:1521/xe')
print(conn.version)
query = 'select*from board'
# select 데이터가 df타입으로 변경되어 갖고온다
df = pd.read_sql_query(query,conn)
df
# 닫기
conn.close()

# Chicken Bowl 2개 이상 주문한 주문 횟수 출력
filt = (df['item_name'] =='Chicken Bowl') & (df['quantity'] >= 2)
len(df[filt]) # 33

# veggie salad bowl 메뉴가 몇번 주문되었는지
df['item_name'].value_counts()
len(df[df['item_name'] =='Veggie Salad Bowl'])
# 가격이 높은순으로 정렬
df[df['item_name'] =='Veggie Salad Bowl'].sort_values('item_price',ascending=False)

## 가장 높은 주문금액에서 item이 총 몇개 팔렸는지
df_price_group = df.groupby('order_id').sum().sort_values('item_price',ascending=False)
df_price_group[['quantity','item_price']]

# items(): 항목과 갯수가 튜플형태로 구성된다
list(df['item_name'].value_counts().items())
item_count = df['item_name'].value_counts() # 아이템, 갯수
for i,(val,cnt) in enumerate(item_count.items()):
    print('rank',(i+1),':',val,':',cnt)
    '''
rank 1 : Chicken Bowl : 726
rank 2 : Chicken Burrito : 553
rank 3 : Chips and Guacamole : 479
rank 4 : Steak Burrito : 368    '''


# agg 함수
df.groupby('grade')['total'].agg(['mean','min','max','sum'])

# 파일로 저장
df.to_csv('../z20_data/score.xlsx',encoding='utf-8-sig')
df.to_csv('../z20_data/score.txt',encoding='utf-8')
df.to_excel('../z20_data/score.xlsx')

### 1. sw특기 에서 각각 단어 소문자로 변경해고, Nan 데이터를 python으로 변경해서 출력
def lower_change(lang):
    # notnull: null이 아닌지 확인, isnull: null인지 확인
    if pd.notnull(lang):# lang가 null이 아니면
        return lang.lower()
    else: return lang
    
df['sw특기'] = df['sw특기'].apply(lower_change)


# 함수를 사용해서 #100점 이상의 국어점수를 100점으로 변경
def add_score(kor):
    kor += 30
    if kor > 100 : kor = 100 # kor 100점 이상이면 100점으로 하겠다.
    return kor
df['국어'] = df['국어'].apply(add_score) # 함수 적용
df

#100점 이상의 국어점수를 100점으로 변경
df['국어'] = df['국어']+20
df['국어']>100 # 조건에 맞으면 True, 아니면 False 로 표현
df.loc[df['국어']>100] = 100

# total 220점 미만이면: 80, 이상이면 60
df['science'] = 0
df.loc[df['total'] < 220,'science'] = 80
df.loc[df['total'] > 220,'science'] = 60
df

# 컬럼명 변경
df.rename(columns={'이름':'name','학교':'school'},inplace=True)
df

# 컬럼 재배열
cols = list(df.columns)
cols

# replace:문자열 처리, strip:공백제거
df['item_price'] = df['item_price'].str.replace("$","").astype(float)

# 조건 &, |
filt  = df['키']>188  #조건식 loc
filt
df.loc[filt]

# 2개 row데이터 출력
df.loc[['1번','5번']]
# 1번학생의 키 값만 출력
df.loc['1번','키']
df.loc['1번',['이름','키']] # 1번 학생의 이름,키 출력
df.loc[['1번','5번'],['이름','키']]
df.loc['1번':'5번','국어':'사회']

# rows데이터 가져오기
df[0:3]
df[5:]
# df[[0,1,3]] #error
df.iloc[[0,1,3]]   # rows데이터 부분적으로 가져오기
df.head()
df.tail(2)

# 컬럼별 호출
df['키']
df['이름']
df[['키','이름']][1:4]
df[df.columns[[1,3,4]]][1:4]
# 컬럼만 가져오기
df.columns
df.columns[0:3]
df.columns[[1,4,6]]

df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()
df['국어'].sum()
df['키'].describe()
df['키'].info()
df['grade'].unique() # 중복제거

df['SW특기'].count() # Nan데이터는 개수에 들어가지 않음.
df['키'].nlargest(4) # 키 큰순으로 3개 가져옴.
df['키'].nsmallest(3) # 키 작은순으로 3개 가져옴

df.describe() # 컬럼별 대략적인 정보, 최소값,최대값,평균 등 확인
df.head()     # 상단 5개 출력
df.tail()     # 하단 5개 출력
df.info()     # 컬럼별 타입,크기 정보
df.values     # rows데이터 배열로 출력
df.index      # index정보
df.columns    # 컬럼 정보
df.shape      # 데이터 크기 