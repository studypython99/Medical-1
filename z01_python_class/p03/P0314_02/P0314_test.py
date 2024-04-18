import random
import time

WORD_LIST = [
    "남박사의 파이썬 프로그래밍 강좌 입니다.",
    "한글 타자 연습해서 타이핑 속도를 높여 보아요.",
    "파이썬은 코드가 짧고 유연하여 가독성과 생산성이 좋은 프로그래밍 언어 입니다.",
    "남박사의 파이썬 동영상 강좌는 인프런에서 볼 수 있습니다.",
    "독도는 우리땅"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    start_time = time.time()
    user_input = input(q + '\n').strip()
    duration = time.time() - start_time

    correct = 0
    for c, a in zip(user_input, q):
        correct = correct + 1 if c == a else correct
    
    src_len = len(q)
    c = correct / src_len * 100
    e = (src_len - correct) / src_len * 100
    speed = float(correct / duration) * 60

    print(f"속도: {speed:0.2f} 정확도: {c:0.2f} % 오타율: {e:0.2f} %")
