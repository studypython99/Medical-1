import matplotlib.pyplot as plt# 시각화 도구 라이브러리
import matplotlib# 그래프 한글설정
import numpy as np
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # for window
# matplotlib.rcParams['font.family'] = 'AppleGothic Gothic' # for mac
matplotlib.rcParams['font.size'] = '15' # 글씨 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스(-)표시

# 그래프 제목
plt.title('막대그래프')
# x,y 축 설명
plt.xlabel('이름',loc='left') # left,center,right
plt.ylabel('국어',loc='top') # top,center,bottom

plt.legend(loc=1,ncol=3)# 범례 표시, 위치설정 / ncol: 한줄에 쓰여지는 갯수
plt.legend(loc=(0.5,0.5)) # 위치값 1,1 사이에서 지정
plt.title('막대그래프',fontdict={})# 그래프 제목
# x,y 축 설명
plt.xlabel('이름',loc='left', color='red') # left,center,right
plt.ylabel('국어',loc='top', color='green') # top,center,bottom

##그래프 그리기, 선두께 linewidth, label:범례
# plt.plot(x,y,linewidth=3,marker='d',markersize=10,markeredgecolor='red',markerfacecolor='yellow',label='국어')
plt.plot(x,y,linewidth=3,marker='d',ms=10,mec='red',mfc='yellow',alpha=0.7,ls=':',label='국어')

plt.figure(figsize=(10,5)) # 그래프 배경크기 설정
plt.yticks([5,10,15,20]) #축의 값을 지정
plt.ylim(175,195) # y축 범위 지정

# 격자무늬 표시, axis 없을시 x,y축 모두 표시 가능
plt.grid(axis='y',ls='--',alpha=0.4)

plt.savefig('g.png') # 저장하기
plt.savefig('g3.png',dpi=3000) # 저장하기 dpi 화질결정
plt.figure(dpi=200) # 보여지는 그래프 전체크기 변경, plt.plot위에 위치해야한다

#bar: 막대그래프 / barh: 옆으로 누운 막대그래프
plt.barh(x,y,label='키')

###y축의 값을 그래프에도 입력해준다
for i, txt in enumerate(y):
    plt.text(x[i],y[i],txt,ha='center',color='blue')

plt.xticks(rotation=45) ## x축 컬럼 45도 기울이기
plt.bar(x,y3,label='국어',width=0.5,alpha=0.5) # width: 막대그래프 폭 조절
                                                # alpha=0.5 투명도

# y축 한개 더 생성                               
fig,ax1 = plt.subplots(figsize=(10,5))
fig.suptitle('출생아수 및 합계출산율') # 상단타이틀 출력
# ax1의 x축은 같이 사용할거에요
ax2 = ax1.twinx()
                                                

# 그래프 2개 이상 사용하기
# ncols=2: 가로로 2개, nrows=2: 세로로 2개
# figsize=(10,5): fig의 (가로,세로)
# sharey=True: y축의 값을 같이 ㅅ ㅏ용
#gridspec_kw={'wspace':0}: 간격0
fig,axs = plt.subplots(ncols=2, figsize=(10,5), sharey=True, gridspec_kw={'wspace':0})
                                                
# values = [30,25,20,13,10,2] #100,꼭 맞출 필요는 없다, 값



###########################   p   i   e   #########################    
filt = df['평점'] >= 9
df[filt]
len(df[filt])
# 9점이상, ~9점미만, ~(not)
values = [len(df[filt]),len(df[~filt])]
title = ['9점 이상', '9점 미만']
exp = [0.1,0]
plt.legend(loc=(1.1,0.5))
plt.pie(values,labels=title,explode=exp,autopct='%.1f%%',startangle=90,counterclock=False)
plt.title('영화 평점 그래프')

values = [1,1,1,1,1,1] # 비율로 맞춰준다
title = ['python','Java','javascript','C#','C','ETC']
explode = [0.2,0,0,0,0,0] # 0.2만큼 조각을 떼어넨다
# startangle=90 : 시작위치 90도부터
# counterclock=False 시계방향으로 하세요
plt.pie(values,labels=title, autopct='%.1f%%', explode=explode,startangle=90, counterclock=False)
pctdistance=0.7 # 글씨를 원의 바깥쪽으로 밀어낸다

# 0516
# y축 색상colorbar, 범위ticks, 크기shrink, 위치orientation='horizontal' 지정
plt.colorbar(ticks=[1,2,3],label='학년',shrink=0.3, orientation='horizontal')