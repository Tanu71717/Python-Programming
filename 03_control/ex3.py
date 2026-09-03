# for

for i in range(10):
    print(i, end=" ")

a = range(5)

print("\n")

print(a.start, a.stop, a.step, sep="\n")

for i in range(1, 11, 2):
    print(i, end=" ")


print("\n")


for i in range(5, 0, -1):
    print(i, end=" ")

num = 0
for i in range(1, 11):
    num += i

print("\n")

print(num)

print(sum(range(1, 11)))

s = "hi한글李浚秀☝️🎮👑"

for c in s:
    print(c, end=" ")

print()


for i in range(1, 10):
    for j in range(1, 10):
        if j == 1:
            print("", end="|| ")
        if (i * j) < 10:
            print(f"{i} * {j} = {i*j}", end="  || ")
        else:
            print(f"{i} * {j} = {i*j}", end=" || ")
    print()
