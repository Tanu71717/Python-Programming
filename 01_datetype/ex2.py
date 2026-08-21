# int, bool, str
# list, tuple, dict, collection

a = 100
print(a, type(a))

print(bin(a), oct(a), hex(a))


print(ord("A"), chr(65))

# x = 10**4299

a = 2**31 - 1
a += 1
print(a)
# print(x)

b = 3.14
print(b, type(b))


c = 0.1 + 0.1 + 0.1
print(c)

import sys

print(sys.float_info.min)
print(sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)

print(0.1 + 0.2)
print(0.2 + 0.1 == 0.3)
print(f"{0.1:.20f}")

print(float(10))
print(int(3.14))
print(float("100"))
print(float("3.1"))
