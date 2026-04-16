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

    def showing(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True
    
    def showing(self) -> None:
        super().showing()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully\n\n")
        else:
            print(f"Rose has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.producing_shade = False

    def produce_shade(self) -> None:
        self.producing_shade = True

    def showing(self) -> None:
        super().showing()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        print(f"[asking the {self.name.lower()} to produce shade]")
        if self.producing_shade:
            print(f"Tree Oak now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide\n\n")
        else:
            print(f"Tree Oak doesn't produce shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.age_and_grow = False

    def growing(self, amount: float) -> None:
        super().growing(amount * 10)
        self.nutritional_value += int(amount * 10)
        self.age_and_grow = True
    
    def aging(self) -> None:
        for i in range(1, self.age + 1):
            super().aging()
        self.nutritional_value += 5
        self.age_and_grow = True

    def showing(self, season: str, days: int) -> None:
        if (self.age_and_grow):
            print(f"[make {self.name.lower()} grow and age for {days} days]")
        super().showing()
        print(f" harvest season: {season}")
        print(f" nutritional value: {self.nutritional_value}")

def ft_plant_types() -> None:
    print(f"=== Garden Plant Type ===")
    flower = Flower("Rose", 25.0, 10, "red")
    print(f"=== Flower ===")
    flower.showing()
    flower.bloom()
    flower.showing()

    print(f"=== Tree ===")
    tree = Tree("Oak", 200.0, 50, 30.0)
    tree.produce_shade()
    tree.showing()

    print(f"=== Vegetable ===")
    vegetable = Vegetable("Carrot", 10.0, 5, "Fall", 50)
    vegetable.showing("April", 10)
    vegetable.growing(2.0)
    vegetable.aging()
    vegetable.showing("May", 20)

if __name__ == "__main__":
    ft_plant_types()
