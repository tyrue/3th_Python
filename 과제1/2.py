var = eval(input("0과 1000사이의 숫자를 입력하세요:")) #문자열을 숫자로 변환한다
one_set = var % 10              # 1의 자리
ten_set = (var % 100) // 10     # 10의 자리
hundred_set = var // 100        # 100의 자리
print("각 자릿수의 합은", one_set+ten_set+hundred_set, "입니다")

