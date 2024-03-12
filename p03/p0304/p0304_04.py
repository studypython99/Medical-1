students = [['홍길동',100,100,100,300,100],
            ['홍길동',100,100,100,300,100],
            ['홍길동',100,100,100,300,100]]     #   2차원 배열, stu 1차원 배열
kors = 0
for stu in students:
    for i in stu:
        kors += stu[1]
print(kors)