name = input("사원이름을 입력하세요: ") # 사원이름
time = eval(input("주당 근무시간을 입력하세요: ")) # 주당 근무시간
pay = eval(input("시간당 급여를 입력하세요: ")) # 시간당 급여
tax_rate = eval(input("원천징수세율을 입력하세요: ")) # 원천징수세율
local_tax = eval(input("지방세율을 입력하세요: ")) # 지방세율
total_pay = time * pay # 총 급여

total_tax = total_pay * tax_rate # 총 급여에서 원천징수세를 계산
total_local = total_pay * local_tax # 총 급여에서 주민서를 계산

print("\n\n사원 이름: {:s}".format(name))
print("주당 근무시간: {:d}".format(time))
print("임금: {:d}".format(pay))
print("총 급여: {:d}".format(total_pay))
print("공제:")

# 원천징수세, 주민세는 폭이 0, 소수점 자리 하나, 백분율로 표시한다. 
print(" 원천징수세 ({:0.1%}): {:d}".format(tax_rate, int(total_tax))) 
print(" 주민세 ({:0.1%}): {:d}".format(local_tax, int(total_local)))
print(" 총 공제: {:d}".format(int(total_tax + total_local)))

print("공제 후 급여: {:d}".format(total_pay - int(total_tax + total_local)))
