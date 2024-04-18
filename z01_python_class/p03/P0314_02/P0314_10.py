#   콜백함수:   함수에서 함수를 다시 부를 수 있다.
def callback_func(h_print):
    for i in range(5):
        h_print()

#   함수선언
def h_print():
    print("안녕하세요.")
    
#   함수호출: 매개변수로 함수를 넘겨주는것
callback_func(h_print)
    
# #   함수호출    
# h_print()

# #   함수를 변수에 저장
# func = h_print