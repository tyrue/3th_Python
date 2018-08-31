import math # 수학 함수를 사용하기 위해 포함

# 오각형 중심에서 꼭짓점까지의 길이
r = eval(input("중심에서 꼭짓점까지의 길이를 입력하세요:")) 
# 한 변의 길이를 구하는 공식
s = 2 * r * math.sin(math.pi / 5)
# 넓이를 계산하는 공식
area = (3 * math.sqrt(3)) / 2 * s**2

print("오각형의 넓이는 ", area,"입니다.")
