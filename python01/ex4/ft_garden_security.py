#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, starting_height: float, starting_age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0

        if not self.set_height(starting_height):
            self._height = 0.0
        if not self.set_age(starting_age):
            self._age = 0

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print(f"Height update rejected")
            return False
        self._height = float(new_height)
        return True

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print(f"Age update rejected")
            return False
        self._age = int(new_age)
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age
    
    def show(self) -> str:
        return f"{self.name}: {self._height}cm, {self._age} years old"


def ft_garden_securty() -> None:
    print(f"== Garden Security System ==")
    my_plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {my_plant.show()}\n")

    if my_plant.set_height(25.0):
        print(f"Height updated: {my_plant.get_height()}")
    if my_plant.set_age(30):
        print(f"Age updated: {my_plant.get_age()}\n")

    my_plant.set_height(-25.0)
    my_plant.set_age(-30)
    my_plant.set_height(25.0)
    my_plant.set_age(30)
    
    print(f"\nCurrent state: {my_plant.show()}")

if __name__ == "__main__":
    ft_garden_securty()