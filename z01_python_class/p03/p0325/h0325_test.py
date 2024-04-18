example = [[1,2,3],[4,[5,6]],7,[8,9]]

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:      #   만약에 아이템의 타입이 리스트라면
            output += flatten(item) #   output에 item을 더해서 넣어두고?
        else:
            output.append(item)     #   아니라면, 아웃풋에 아이템을 넣어둔다?
    return output

print(flatten(example))