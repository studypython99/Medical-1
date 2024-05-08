def first(win_num):
    # win_num = []            #   이 자리는 지역변수, 자리가 따로 만들어진다. 리턴으로 돌리지 않으면
    for i in range(5):      #   계속 빈값이 된다.
        win_num.append(i)
    

win_num = []    #   이것만 있으면 01234, 0123401234, 01230123401234 ....진행
while True:
    input("다시 실행할까요?")
    first(win_num)
    print("win_num데이터: ",win_num)
    win_num = []    #   여기에 한번 더 작성해서 초기화, 공백으로 만듦
