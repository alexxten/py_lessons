a = 1

if a == 1:
    print("a == 1")
elif a == 2:
    print("a == 2")
else:
    print("WOW that not 1 or 2")


if a == 1:
    print("a == 1")
    a += 1
elif a == 1:
    print("a == 2")
    a += 2

b = a + 100
print(b)