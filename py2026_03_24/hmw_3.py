##Задание 1 Создайте класс Animal, который при инициализации принимает:


class Animal:
    def __init__(self, name: str, age: int, hunger_level: int = 50):
        print("CALLED INIT")
        self.name = name
        self.age = self.value_check(age)
        self.hunger_level = self.value_check(hunger_level)

    def __new__(cls, *args, **kwargs):
        print("CALLED NEW")
        return super().__new__(cls)

    def value_check(self, arg):
        if arg <= 0:
            raise ValueError("Hunger or Age values cannot be a negative number.")
        elif arg > 100:
            raise ValueError("Hunger or Age values cannot be greater than 100.")
        else:
            return arg

    def make_sound(self):
        return "Животное издаёт звук"

    def move(self):
        return f"{self.name} двигается"

    def eat(self):
        if self.hunger_level < 10:
            self.hunger_level = 0
        else:
            self.hunger_level = self.hunger_level - 10
        return f"{self.name} поел. Голод: {self.hunger_level}"

    def get_info(self):
        return f"{self.name}, возраст: {self.age} лет, голод: {self.hunger_level}"


animal_bayun = Animal(name="Bayun", age="4")
print(animal_bayun.make_sound())
# print(animal_bayun.move())
# print(animal_bayun.eat())
# print(animal_bayun.get_info())
#
# animal_arcasha = Animal(name="Arkasha", age=37, hunger_level=-7)
# print(animal_arcasha.eat())
# print(animal_arcasha.get_info())


##Задание 2. Реализуйте дочерний класс Lion (наследует Animal):


class Lion(Animal):

    def make_sound(self):
        return f"Рррр! Рык льва!"

    def move(self):
        return f"{self.name} грациозно крадётся"

    def hunt(self):
        if self.hunger_level > 80:
            self.hunger_level = 100
        else:
            self.hunger_level = self.hunger_level + 20
        return f"{self.name} охотится!"

#
# lion_timusya = Lion(name="Timusya", age=3, hunger_level=8)
# print(lion_timusya.hunt())
# print(lion_timusya.get_info())
# print(lion_timusya.hunt())
# print(lion_timusya.get_info())
