import time # 시간함수를 사용하기위해 포함
offset = eval(input("GMT와 시간대 차이를 입력하세요:"))
currentTime = time.time() # 현재 시간(초)을 얻어온다.

# 1970년 1월 1일 자정 이후로의 전체 초 값을 얻어온다.
totalSeconds = int(currentTime)

currentSecond   = totalSeconds  % 60    # 현재 시간의 초 값을 계산
totalMinutes    = totalSeconds // 60    # 전체 분 값을 계산
currentMinutes  = totalMinutes  % 60    # 현재 분 값을 계산
totalHours      = totalMinutes // 60    # 전체 시 값을 계산
currentHours    = totalHours    % 24    # 현재 시 값을 계산

print("현재 시간은", currentHours-offset,":",currentMinutes,":",currentSecond,"입니다")
