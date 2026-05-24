import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response)
print(response.status_code)
print(response.json())

with open("test.txt", "w") as f:
    f.write(response.text)

with open("test.txt", "r") as f:
    f_readlines = f.readlines()

with open("test.txt", "r") as f:
    f_read = f.read()

print(f_read, type(f_read))
print(f_readlines, type(f_readlines))

# так не делаем - файл можно считать только единожды!
with open("test.txt", "r") as f:
    f_readlines = f.readlines()
    f_read = f.read()


