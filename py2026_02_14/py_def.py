# y = 4x + 1

def count_expression(x: int | float) -> int | float:
    y = 4 * x + 1
    return y

for i in range(10):
    result = count_expression(i)
    print(f"{i} - {result}")