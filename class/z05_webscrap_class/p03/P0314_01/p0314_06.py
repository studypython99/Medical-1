a_list = [1,2,3]
try:
    print(a_list)
    print(1/0)
    txt = int(input("숫자를 입력하세요 >>"))
    print(txt)
    raise # 에러발생, 강제 에러발생
except Exception as e:  #   예외의 종류가 다양하다, 
    print("예외가 발생했습니다.")
    print('타입:',type(e))