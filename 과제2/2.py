import math # 수학 함수를 사용하기위해 포함
n = eval(input("변의 개수를 입력하세요:")) # 변의 개수
s = eval(input("변의 길이를 입력하세요:")) # 변의 길이

area = (n * s**2) / (4 * math.tan(math.pi/n)) # 정다각형의 넓이

print("다각형의 넓이는 ", area, "입니다.")
