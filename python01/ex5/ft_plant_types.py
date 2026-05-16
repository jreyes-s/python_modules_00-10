#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growing(self) -> None:
        self.height += 20

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
            print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str, height: float, age: int, trunk: float) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.producing_shade = False

    def produce_shade(self) -> None:
        self.producing_shade = True

    def showing(self) -> None:
        super().showing()
        print(f" Trunk diameter: {self.trunk}cm")
        print(f"[asking the {self.name.lower()} to produce shade]")
        if self.producing_shade:
            print(f"Tree Oak now produces a shade of "
                  f"{self.height}cm long and {self.trunk}cm wide\n\n")
        else:
            print("Tree Oak doesn't produce shade")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float, age: int, season: str, nut_val: int) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nut_val = nut_val
        self.age_and_grow = False

    def growing(self) -> None:
        super().growing()
        self.height += 22
        self.nut_val += 15
        self.age_and_grow = True

    def aging(self) -> None:
        self.age += 20
        self.nut_val += 5
        self.age_and_grow = True

    def showing(self, season: str = "Unknown", days: int = 0) -> None:
        if (self.age_and_grow):
            print(f"[make {self.name.lower()} grow and age for {days} days]")
        super().showing()
        print(f" harvest season: {season}")
        print(f" nutritional value: {self.nut_val}")


def ft_plant_types() -> None:
    print("=== Garden Plant Type ===")
    flower = Flower("Rose", 15.0, 10, "red")
    print("=== Flower ===")
    flower.showing()
    flower.bloom()
    flower.showing()

    print("=== Tree ===")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.produce_shade()
    tree.showing()

    print("=== Vegetable ===")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.showing("April", 10)
    vegetable.growing()
    vegetable.aging()
    vegetable.showing("May", 20)


if __name__ == "__main__":
    ft_plant_types()
