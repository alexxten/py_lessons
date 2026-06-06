a = 1
b = "some_string"

def c() -> None:
    print("Hello World")


class Human:
    def __init__(self, name: str, age: int = 18) -> None:
        self.name = name
        self.age = age

    def sleep(self) -> None:
        print("Sleeping, bye")

    def say_name(self) -> None:
        print(f"Hello, my name is {self.name}!")

    def say_all_about_me(self) -> None:
        print(f"{self.name, self.age}")


class Zumer(Human):
    def __init__(self, name: str, elektronka: str, age: int = 18) -> None:
        super().__init__(name, age)
        self.elektronka = elektronka

    def my_killer(self) -> None:
        print(f"I kill myself with {self.elektronka}")
#
# human_ann = Human(name="Аня")
# human_vova = Human(name="Вова", age=25)
# human_ann.say_name()
# human_vova.say_name()
# print(human_vova.name, human_vova.age)
# human_ann.say_all_about_me()

zumer_olesha = Zumer(name="Olesha", age="19", elektronka="IQOS")
zumer_olesha.my_killer()
zumer_olesha.sleep()
zumer_olesha.say_all_about_me()




# Тут мои страдания

class Animal:
    def __init__(self, amt_legs: int, fur: bool, description: str):
        self.amt_legs = amt_legs
        self.fur = fur
        self.description = description

    def my_legs_count(self) -> None:
        print(f'I have {self.amt_legs} legs')

animal_cat = Animal(amt_legs = 4, fur = True, description = 'angry creature')

animal_cat.my_legs_count()

print(animal_cat.description)
