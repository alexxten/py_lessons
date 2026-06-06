def get_age_category(age):
    if age < 0:
        return "Ошибка"
    elif age <= 2:
        return "Младенец"
    elif age <= 12:
        return "Ребенок"
    elif age <= 19:
        return "Подросток"
    elif age <= 35:
        return "Молодой"
    elif age <= 60:
        return "Взрослый"
    else:
        return "Пожилой"


def can_vote(age):
    if age >= 18:
        return "Может голосовать"
    else:
        return "Не может голосовать"


def save_to_file(name, age, category, vote_status):
    file = open("people.txt", "a")
    file.write(
        name + " | " + str(age) + " лет | " + category + " | " + vote_status + "\n")
    file.close()
    print("Данные сохранены в файл!")


def show_all_people():
    file = open("people.txt", "r")
    content = file.read()
    if content == "":
        print("Файл пуст")
    else:
        print("=== Все записи ===")
        print(content)
    file.close()


def main():
    print("Программа определения возраста")

    while True:
        print("\n1. Добавить человека")
        print("2. Показать всех")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Имя: ")
            age = int(input("Возраст: "))

            category = get_age_category(age)

            if category == "Ошибка":
                print("Возраст не может быть отрицательным!")
            else:
                vote = can_vote(age)
                print(name + " - " + category)
                print("Статус голосования: " + vote)
                save_to_file(name, age, category, vote)

        elif choice == "2":
            show_all_people()

        elif choice == "3":
            print("Пока!")
            break
        else:
            print("Неверный выбор")


# Запуск программы
main()