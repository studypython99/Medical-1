num = [[10,20],[30,40],[50,60]]
while True:
    for i in range(len(num)):
        for j in range(len(num[i])):
            print(num[i][j])    #   10,20,30,40
            
    i = 0
    while i < len(num):
        j = 0
        while j < len(num[i]):
            print(num[i][j])
            j = j+1
        i += 1