#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display_statistics(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")
            

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats = Plant.Statistics()

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 315:
            return True
        return False

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def growing(self, amount: int) -> None:
        self.height += amount
        self.stats.grow_calls += 1

    def aging(self) -> None:
        self.age += 1
        self.stats.age_calls += 1

    def showing(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.show_calls += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        self.growing(5)
    
    def showing(self) -> None:
        super().showing()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully")
        else:
            print(f" Rose has not bloomed yet")
        self.stats.show_calls += 1
        self.statistics_show()

    def statistics_show(self) -> None:
        print(f"[statistics for {self.name}]")
        self.stats.display_statistics()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 315


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0
        self.producing_shade = False

    def produce_shade(self) -> None:
        self.shade_count += 1
        print(f"Tree Oak now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide")
        self.statistics_show()

    def showing(self) -> None:
        super().showing()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        self.stats.show_calls += 1
        self.statistics_show()

    def statistics_show(self) -> None:
        print(f"[statistics for {self.name}]")
        self.stats.display_statistics()
        print(f" {self.shade_count} shade")


class Anonymous(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.age_and_grow = False

    def growing(self, amount: int) -> None:
        super().growing(amount * 10)
        self.nutritional_value += int(amount * 10)
        self.age_and_grow = True
        self.stats.grow_calls += 1
    
    def aging(self) -> None:
        for i in range(1, self.age + 1):
            super().aging()
        self.nutritional_value += 5
        self.age_and_grow = True
        self.stats.age_calls += 1

    def showing(self, season: str, days: int) -> None:
        if (self.age_and_grow):
            print(f"[make {self.name.lower()} grow and age for {days} days]")
        super().showing()
        print(f" harvest season: {season}")
        self.stats.show_calls += 1


def ft_garden_analytics():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()

    print("=== Flower")
    flower = Flower('Rose', 15.0, 10, "red")
    flower.showing()
    flower.bloom()
    print(f'[asking the {flower.name.lower()} to grow and bloom]')
    flower.showing()
    print()

    print("=== Tree")
    tree = Tree('Oak', 200.0, 365, 5)
    tree.showing()
    print(f"[asking the {tree.name.lower()} to produce shade]")
    tree.produce_shade()
    print()
    

if __name__ == "__main__":
    ft_garden_analytics()
