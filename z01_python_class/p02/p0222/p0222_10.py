#   지폐 교환 프로그램

# money=input("교환할 돈을 입력하세요 >> ")
# money=int(money)

# 돈을 입력(입금)하면, 500/100/50/10원의 동전갯수 구하기
#     억 천 만 십만 천 백 십 원
insertcoin=int(input("입금하세요 >> "))
c500=insertcoin//50000
c100=insertcoin%50000//10000
c50=insertcoin%50000%10000//5000
c10=insertcoin%50000%10000%5000//1000

print('{}원 입금하시면\n5만원권\t{}개\n1만원권\t{}개\n5천원권\t{}개\n1천원권\t{}개'
      .format(insertcoin,c500,c100,c50,c10))