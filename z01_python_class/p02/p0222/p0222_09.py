#   동전 교환 프로그램

# money=input("교환할 돈을 입력하세요 >> ")
# money=int(money)

# 돈을 입력(입금)하면, 500/100/50/10원의 동전갯수 구하기

insertcoin=int(input("입금하세요 >> "))
c500=insertcoin//500
c100=insertcoin%500//100
c50=insertcoin%500%100//50
c10=insertcoin%500%100%50//10
print('{}원 입금하시면\n500원\t{}개\n100원\t{}개\n50원\t{}개\n10원\t{}개'
      .format(insertcoin,c500,c100,c50,c10))