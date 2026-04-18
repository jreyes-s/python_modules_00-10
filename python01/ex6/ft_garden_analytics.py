#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")


    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = round(float(height), 1)
        self.age = age
        self._stats = Plant.Statistics()
        self.shade_calls = None

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls):
        """Creates a plant with default/unknown info."""
        return cls("Unknown plant", 0.0, 0)

    def growing(self, increment: float = 8.0) -> None:
        self.height += increment
        self._stats.grow_calls += 1

    def aging(self) -> None:
        for _ in range(20):
            self.age += 1
        self._stats.age_calls += 1

    def showing(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self._stats.show_calls += 1

def display_plant_analytics(plant: Plant) -> None:
    """Unique function, not part of any class, to display stats."""
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if plant.shade_calls is not None:
        print(f" {plant.shade_calls} shade")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def growing(self, increment: float = 8.0) -> None:
        super().growing(increment)
    
    def showing(self) -> None:
        super().showing()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        for _ in range(42):
            self.seed_count += 1

    def showing(self) -> None:
        super().showing()
        print(f" Seeds: {self.seed_count}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = round(float(trunk_diameter), 1)
        self.shade_calls = 0

    def produce_shade(self) -> None:
        self.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide")

    def showing(self) -> None:
        super().showing()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


def ft_garden_analytics():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()

    print("=== Flower")
    rose = Flower('Rose', 15.0, 10, "red")
    rose.showing()
    rose.bloom()
    display_plant_analytics(rose)
    rose.growing()
    print(f'[asking the {rose.name.lower()} to grow and bloom]')
    rose.showing()
    display_plant_analytics(rose)
    print()

    print("=== Tree")
    oak = Tree('Oak', 200.0, 365, 5)
    oak.showing()
    display_plant_analytics(oak)
    print(f"[asking the {oak.name.lower()} to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.showing()
    print(f"[make {sunflower.name.lower()} grow, age and bloom]")
    sunflower.growing(30.0)
    sunflower.aging()
    sunflower.bloom()
    sunflower.showing()
    display_plant_analytics(sunflower)

if __name__ == "__main__":
    ft_garden_analytics()
