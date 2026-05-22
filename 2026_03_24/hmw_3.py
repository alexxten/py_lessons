##Задание 1 Создайте класс Animal, который при инициализации принимает:

class Animal:
  def __init__(self, name:str, age:int, hunger_level:int = 50):
    self.name = name
    self.age = age
    self.hunger_level = hunger_level
    ##Тут нужно ставить ограничение??????????
    ##Тип:
    ##if 0 <= self.hunger_level <= 100:
    ##  self.hunger_level = hunger_level
    ##else:
    ##  print(f"Возраст животного может быть только от 0 до 100.")

  def make_sound(self):
    print('Животное издаёт звук')

  def move(self):
    print(f"{self.name} двигается")

  def eat(self):
    if self.hunger_level < 10:
      self.hunger_level = 0
    else:
      self.hunger_level = self.hunger_level - 10
    print(f"{self.name} поел. Голод: {self.hunger_level}")

  def get_info(self):
    print(f"{self.name}, возраст: {self.age} лет, голод: {self.hunger_level}")

animal_bayun = Animal(name="Bayun", age="4")
animal_bayun.make_sound()
animal_bayun.move()
animal_bayun.eat()
animal_bayun.get_info()

animal_arcasha = Animal(name = "Arkasha", age = 37, hunger_level= -7)
animal_arcasha.eat()
animal_arcasha.get_info()
##Задание 2. Реализуйте дочерний класс Lion (наследует Animal):

class Lion(Animal):

    def make_sound(self):
        print(f"Рррр! Рык льва!")

    def move(self):
        print(f"{self.name} грациозно крадётся")

    def hunt(self):
        if self.hunger_level > 80:
            self.hunger_level = 100
        else:
            self.hunger_level = self.hunger_level + 20

        print(f"{self.name} охотится!")

lion_timusya = Lion(name = 'Timusya', age = 3, hunger_level = 8)
lion_timusya.hunt()
lion_timusya.get_info()
lion_timusya.hunt()
lion_timusya.get_info()