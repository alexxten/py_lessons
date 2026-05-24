import random

a = random.randint(1, 4)

if a == 1:
    print("a is 1")
elif a == 2:
    print("a is 2")
elif a == 3:
    print("a is 3")


match a:
    case True:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is smth else")


a = []
print(bool(a))