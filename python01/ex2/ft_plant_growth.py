#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def update_age(self) -> None:
        self.age += 1

    def show(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    initial_height: float = 25.0
    plant = Plant("Rose", initial_height, 30)
    print("=== Garden Plant Growth ===")
    print(plant.show())
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.update_age()
        print(f"{plant.show()}")

    total_growth: float = round(plant.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
