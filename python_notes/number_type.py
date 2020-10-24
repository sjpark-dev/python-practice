# 수 자료형 #

a = 1e9  # 1000000000.0 (10억)

a = 1e-3  # 0.001

a = 0.3 + 0.6  # 0.8999999999999999
a = round(a, 4)  # 0.9

a = round(123.456, 2)  # 123.46
a = round(1.4)  # 1
a = round(1.6)  # 2
# 실수 round()시에 정확이 반이면 가까운 짝수로 변환
a = round(1.5)  # 2
a = round(2.5)  # 2
# 해결책
a = round(1.5+0.5)  # 2
a = round(2.5+0.5)  # 3

a = 4 / 2  # 2.0 (나누기 연산자를 사용하면 실수형으로 변환)
a = 4 // 2  # 2 (몫 연산자)
a = 4 % 2  # 0 (나며지 연산자)
a = 2 ** 3  # 8 (거듭제곱 연산자)
