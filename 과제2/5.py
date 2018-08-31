price = eval(input("물건값을 입력하시오: ")) # 물건의 가격
thousand = 1000 * eval(input("1000원 지폐개수: ")) # 1000원 개수
f_hundred = 500 * eval(input("500원 동전개수: ")) # 500원 개수
hundred = 100 * eval(input("100원 동전개수: ")) # 100원 개수

money = thousand + f_hundred + hundred - price # 거스름돈 전체
f_hundred = money // 500 # 500원 동전의 개수
money -= 500 * f_hundred # 500원 동전만 뺀 나머지 거스름돈
hundred = money // 100 # 100원 동전의 개수
money -= 100 * hundred # 100원 동전만 뺀 나머지 거스름돈
ten = money // 10 # 10원 동전의 개수
money -= 10 * ten # 10원 동전만 뺀 나머지 거스름돈 = 1원 동전 개수

print("500원= {:d} 100원= {:d} 10원= {:d} 1원= {:d}".format(f_hundred, hundred, ten, money))
