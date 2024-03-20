a_list = [
    1,2,[3,4],5,[6,7,8,9],[10,11]
]

for a in a_list:
    if type(a) == list:
        for i in a:        
            print(i,end=" ")
    else:
        print(a,end=" ")
#결과: 1 2 3 4 5 6 7 8 9 10 11 