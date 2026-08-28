# 산술
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a**b)

# 복합 대입 연산자
a = 4
a += 4
print(a)

# 증강 연산자
a += 1

# 비교 연산자
print(3 == 1.0 + 1.0 + 1.0)
print(3 >= 3)
print(3 <= 3.0)
print(3 != 3.0)
print("apple" < "apble")
print(1 < 2 < 3)  # 1 < 2 and 2 < 3
print(1 < 3 < 2)  # 1 < 3 and 3 < 2

# 논리 연산자 (and, or, not)

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)

# short-circuit 테스트
a = 10
b = 0
# print(a/b)

if a > 0 or a / b:
    print("짧은 길!")
