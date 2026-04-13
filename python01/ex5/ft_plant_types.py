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
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True
    
    def showing(self) -> None:
        print("=== Flower")
        print(super().showing())
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"Rose has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.producing_shade = False

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.producing_shade = True

    def showing(self) -> None:
        print("=== Tree")
        print(super().showing())
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        if self.producing_shade:
            print(f"Tree Oak now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide")
        else:
            print(f"Tree Oak doesn't produce shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0


def ft_plant_types() -> None:
    print(f"=== Garden Plant Type ===")

if __name__ == "__main__":
    ft_plant_types()
