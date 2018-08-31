money, rate = eval(input("잔고와 연이율을 입력하세요(예. 3%는 3으로):")) # 잔고, 연이율
interest = money * (rate / 1200) # 다음 달 상환금 이자
print("이자는", interest, "입니다.")
