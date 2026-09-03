# 반복문 for while

# while

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("OVER")

num = [1, 2, 3, 4, 5]
target = 2
i = 0

while i <= 4:
    if num[i] == target:
        print("find target")
        break
    i += 1
else:
    print("not find target")


i = 0
target = 2321
temp = 0
while i <= 4:
    if num[i] == target:
        print("find target")
        temp += 1
        break
    i += 1
if not temp == 1:
    print("not find target")

i = 0
num = 0
while i <= 10:
    num += i
    i += 1
print(num)


i = 0
num = 0
while i <= 10:
    if i % 2 == 0:
        num += i
    i += 1
print(num)
