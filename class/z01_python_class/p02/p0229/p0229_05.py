#   continue: 반복문에서 남은 문장을 수행하지 않고 다음단계로 넘어간다.

n = 0
while n < 100:
    n += 1
    if n % 2 == 0:  #   짝수일 때
        continue    #   건너뛴다
    print(n,end=' ')
    
breakletter = input('중단문자')
for letter in 'python':
    if letter == breakletter:
        continue
    print(letter)
    
#   break:      문자를 만나면 프로그램이 종료
#   continue:   ffff
#   pass:       ffff
#   즉, 어떤 것도 수행하지 않고 해당부분을 pass