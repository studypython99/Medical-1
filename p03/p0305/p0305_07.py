aa = [[1,[3,4,5],3,4],[5,6],[7,8,9]]
aaa = [[[1,2],3,4,5],[[6][7,8,9]]]
a = [1,2,3,4,5]
for i in a:
    print(i)
print('-'*50)
for i in aa:
    for j in i:     #   여기까지는 모두 적용, aa[0][1] = [3,4,5]는 혼자만 3차원 배열
        if isinstance(j, list): #   리스트인지 확인해준다
            for k in j:     #   aa[1] 부터는 3차원이 없다.
                print(k)    #   2차원 배열을 꺼내려면 for문을 두번 사용한다
        else:
            print(j)
            