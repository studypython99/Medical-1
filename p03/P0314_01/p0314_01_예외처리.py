#   예외처리 try catch
#   구문오류: 프로그램 실행 전에 발생하는 오류 ex) print() 에서 print(  처럼 닫는 괄호가 없는 경우
#   런타임오류: 프로그램 실행 중에 발생하는 오류 ex) 아래의 경우 6 이상 입력했을 경우, 범위를 벗어남

#   예외처리시, 오류가 발생되어도
#   프로그램이 종료되지 않는다
#   모두 try로 만들면 어디가 오류인지 알 수 없게된다.
#   웬만하면 사용x, if문을 사용해서 오류 없도록 한다.
try:    #   오류가 발생될것 같은 지점에 사용하면
    num = int(input("숫자입력하세요 >>"))
    a_list = [1,2,3,4,5]
    for i in range(num):
        print(a_list[i])
except: #   여기로 넘어온다
    print("구문에 오류가 났습니다.")
    