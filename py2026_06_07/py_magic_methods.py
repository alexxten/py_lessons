def __init__():
    ...

class Spell:
    def __init__(self, name: str, strength: int) -> None:
        self.name = name
        self.strength = strength

    def __eq__(self, other):
        return self.strength == other.strength

    def __gt__(self, other):
        return self.strength > other.strength



spell_fire = Spell("Fire", 10)
spell_water = Spell("Water", 10)

a = 1
b = 1
print(spell_fire == spell_water)

def __eq__():
    ...

def __lt__():
    ...

def __gt__():
    ...

def __bool__():
    ...

a_lst = [1, 2]
# print(dir(a_lst))