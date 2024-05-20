{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import svm,metrics\n",
    "from sklearn.model_selection import train_test_split\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib\n",
    "import random\n",
    "matplotlib.rcParams['font.family'] = 'Malgun Gothic'\n",
    "matplotlib.rcParams['font.size'] = 10\n",
    "matplotlib.rcParams['axes.unicode_minus'] = False"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. 데이터 전처리\n",
    "### 2. 데이터 학습시키기\n",
    "### 3. 데이터 예측\n",
    "### 4. 정답률 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 150 entries, 0 to 149\n",
      "Data columns (total 5 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   SepalLength  150 non-null    float64\n",
      " 1   SepalWidth   150 non-null    float64\n",
      " 2   PetalLength  150 non-null    float64\n",
      " 3   PetalWidth   150 non-null    float64\n",
      " 4   Name         150 non-null    object \n",
      "dtypes: float64(4), object(1)\n",
      "memory usage: 6.0+ KB\n"
     ]
    }
   ],
   "source": [
    "# 파일 불러오기\n",
    "df = pd.read_csv('../z20_data/02.iris.csv')\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 데이터 전처리: train_data, test_data\n",
    "#   문제와 답을 분리\n",
    "# 2. 데이터 학습시키기\n",
    "# 3. 데이터 예측하기\n",
    "# 4. 데이터 결과, 정답률"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # 파이썬 random 함수\n",
    "# ran = [i for i in range(150)]\n",
    "# random.shuffle(ran)\n",
    "# ran\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 25  64 106 146  88  82 103  78  57  65 118   3   5 136  14  81 126 130\n",
      " 121 134 127  83 105   2  18  16 112  92   7  11  58  74 100 116  38  90\n",
      "  45  31  51 102 129 142 107  40  79 122  87  67   8  10 139  71  39  80\n",
      " 128 124  50 138 120 135 147  84 144  62 104   1  75  73  56  47  48  85\n",
      "  53  61   4  23   9  63  21  26  37  44  96 101  20  41 113  36  91  46\n",
      " 143  98 125  86  68 114  42  99 145  27  43 111 115  89  94 109  28  77\n",
      " 132   0  76  72  52  33   6  15  12  24 119  17 110  66 149 141  95 117\n",
      "  13 123  93  59 148  55  60  97 140  32 137 131  22  54 133  29  30  35\n",
      "  49  34  70  19  69 108]\n"
     ]
    }
   ],
   "source": [
    "# numpy random 함수, 데이터 순서를 랜덤으로 변경\n",
    "index = np.arange(150)\n",
    "np.random.shuffle(index)\n",
    "print(index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 자동으로 train, test데이터를 분리해준다\n",
    "# from sklearn.model_selection import train_test_split\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 데이터 전처리: train_data, test_data\n",
    "# random code: 0~149 랜덤숫자 생성, index로 df에 대입.\n",
    "\n",
    "#   문제와 답을 분리\n",
    "# df[['SepalLength','SepalWidth','PetalLength','PetalWidth']] # 문제\n",
    "# df['Name'] # 답"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# train_input rows 100개를 출력하시오, 나머지 50개 나눠서 저장하기\n",
    "# iloc(row, comumns)\n",
    "# train_input = df.iloc[index[:100],:-1]\n",
    "# test_input = df.iloc[index[100:],:-1]\n",
    "# # # df[['SepalLength','SepalWidth','PetalLength','PetalWidth']][:100] # 문제\n",
    "# # # df[['SepalLength','SepalWidth','PetalLength','PetalWidth']][100:] # 문제\n",
    "\n",
    "\n",
    "# # # train_target rows 100개를 출력하시오, 나머지 50개 나눠서 저장하기\n",
    "# train_target = df.iloc[index[:100],4]\n",
    "# test_target = df.iloc[index[100:],4]\n",
    "# df['Name'][:100] # 답\n",
    "# df['Name'][100:] # 답"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "datas_input = df.iloc[:,:-1]# name제외한 앞 컬럼들\n",
    "datas_target = df.iloc[:,4]# name 컬럼"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 자동으로 train, test데이터를 분리해준다\n",
    "from sklearn.model_selection import train_test_split\n",
    "train_input, test_input, train_target, test_target = train_test_split(datas_input,datas_target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정답률:  0.8947368421052632\n"
     ]
    }
   ],
   "source": [
    "# 2. 데이터 학습시키기\n",
    "clf = svm.SVC()\n",
    "# 데이터 훈련\n",
    "clf.fit(train_input,train_target)\n",
    "\n",
    "# 3. 데이터 예측, 데이터 추가: test_input\n",
    "result = clf.predict(test_input)\n",
    "\n",
    "# 4. 정답률\n",
    "score = metrics.accuracy_score(test_target,result)\n",
    "print('정답률: ',score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "답:  ['Iris-setosa' 'Iris-versicolor' 'Iris-versicolor']\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\KOREAVC\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\base.py:493: UserWarning: X does not have valid feature names, but SVC was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "# 3. 데이터 예측, 데이터 추가: test_input\n",
    "data1 = [4.9,2.9,1.4,0.2]\n",
    "data3 = [5.9,1.9,2.4,1.2]\n",
    "data2 = [2.9,0.9,3.4,0.2]\n",
    "data4 = [data1,data3,data2]\n",
    "result = clf.predict(data4)\n",
    "print('답: ',result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
