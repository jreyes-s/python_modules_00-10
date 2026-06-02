#!/usr/bin/env python3

from typing import Any


class Plant:
    def __init__(self, name: str, height: Any, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
