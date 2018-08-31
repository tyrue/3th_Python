import math # 수학함수 sqrt를 사용하기위해 포함
x1, y1, x2, y2, x3, y3 = eval(input("삼각형의 세 꼭지점을 입력하세요:"))
s1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # 변1
s2 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2) # 변2
s3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2) # 변3
s = (s1 + s2 + s3)/2                        # 넓이 공식을 위한 수
area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3)) # 넓이를 구하는 공식
print("삼각형의 넓이는 ", area, "입니다")

