from typing import Any, Callable
import pandas as pd


def somefunc(a: int, b: int) -> int:
    return a + b

def somefunc_kwargs(*, a:int, b:int) -> int:
    return a + b

def somefunc_args_kwargs(a:int, b:int, *, c: int) -> int:
    return a + b + c

print(somefunc(1, 2))
print(somefunc(b=2, a=1))
print(somefunc_kwargs(b=1, a=2))
print(somefunc_args_kwargs(5, 6, c=6))

# позиционные аргументы - args, именованные аргументы - kwargs

def somefunc_with_true_args_kwargs(*args, **kwargs) -> tuple:
    for i in args:
        print(i)
    return f"args: {type(args)}, {args}", f"kwargs: {type(kwargs)}, {kwargs}"

print(somefunc_with_true_args_kwargs(1, 2, 5, 6, 7, c=3, k=6, uiyiyiyi=8))

# функции высшего порядка
def somefunc_as_obj() -> int:
    return 2**5

def highlevel_func(fn: Callable, myarg: int) -> Any:
    return fn() + myarg

print(highlevel_func(somefunc_as_obj, myarg=4))

# lambda

somefunc_as_obj_with_lambda = lambda : 2**5
print(somefunc_as_obj_with_lambda())

somefunc_as_obj_with_lambda_and_arg = lambda x, y: x**y
print(somefunc_as_obj_with_lambda_and_arg(2, 6))


df_sales = pd.DataFrame({
    'product': ['Ноутбук', 'Смартфон', 'Планшет', 'Монитор', 'Клавиатура'],
    'price': [50000, 30000, 20000, 15000, 3000],
    'quantity_sold': [50, 120, 80, 45, 200],
    'discount_rate': [0.1, 0.05, 0.15, 0.2, 0],
    'email': ['Ноутбук@mail.ru', 'Смартфон@mail.ru', 'Планшет@mail.ru', 'Монитор@mail.ru', 'Клавиатура@mail.ru'],
})

df_sales['revenue_before_discount'] = df_sales.apply(
    lambda row: row['price'] * row['quantity_sold'], axis=1
)

df_sales['test'] = df_sales.apply(
    lambda row: row['email'].split("@"), axis=1
)

print(df_sales)


