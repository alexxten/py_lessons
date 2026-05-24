import random

for i in range(5):
    print(i)


i = 4
while i > 0:
    print(i)
    i -= 1

some_arg = 1
some_arg2 = 1
while some_arg * some_arg2 == 1:
    print("i'm here")



a = 30
b = 50
while a > 0 and b > 0:
    print(f"{a=}, {b=}, cond True")
    c = random.randint(30, 100)
    b -= c
    a -= c
    if a < 10:
        break

print(f"{a=}, {b=}, {c=}")


# while True:
#     print("b")
