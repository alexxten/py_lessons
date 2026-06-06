import os.path


if not os.path.exists("g"):
    print("no file")
else:
    with open("g") as f:
        f.read()

print("------")

try:
    with open("g") as f:
        f.read()
except Exception as e:
    print(e, type(e))
finally:
    print("finally here")


class CustomException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


try:
    a = 1
    raise CustomException("my fucking exception")
except CustomException as e:
    print(e)
finally:
    print("wow")


def first_func():
    a = 8
    b = 9
    raise CustomException("oh nooo error")

def main_func():
    first_func()


def view():
    try:
        main_func()
        print("it's ok")
    except Exception as e:
        print(e)


view()
