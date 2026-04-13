#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growing(self, amount) -> None:
        self.height += amount

    def aging(self) -> None:
        self.age += 1

    def showing(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        self.is_blooming = False
        print(f"[asking the rose to bloom]")
    
    def showing(self) -> None:
        print("=== Flower")
        print(super().showing())
        print(f" Color: {self.color}")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> bool:
        if self.trunk_diameter >= 5:
            print(f"[asking the oak to produce shade]")
            print(f"Tree Oak now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
            return True
        return False

    def showing(self) -> None:
        print("=== Tree")
        print(super().showing())

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0


def ft_plant_types() -> None:
    print(f"=== Garden Plant Type ===")

if __name__ == "__main__":
    ft_plant_types()
