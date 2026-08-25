a = "python"
b = "python"

print(a, type(a))
print(b, type(b))

print("I'll be back")

m = """
dddddd
ddddddddd
ssssssssssss
dssssssss
dssssssssss
fdfwe
wef
ewfewfewfewfwefef
wef
ewfwefwf"""

print(m)


def fun():
    """이 함수는 테스트 용이다"""
    pass


print(fun.__doc__)


print("add" + "ddh")
print("ㅁㄷㅊㅇ" * 200)

print("hello" + str(2))
k = "10" + "2"
print(k[0] + k[2])


name = "pororo"
age = 23
print(f"이름 : {name}, 나이 : {age}")
print(f"내년 나이 : {age+1}")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.1f}")
print(f"{pi:.3f}")

num = 123456789
print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:<15d}")
print(f"{num:015,d}")
