#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, starting_height: float, starting_age) -> None:
        self.name = name
        self.starting_height = starting_height
        self.starting_age =  starting_age

    def show(self) -> str:
        return(f"{self.name}: {self.starting_height}cm, {self.starting_age} days old")


def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)
    print("== Plant Factory Output ==")
    print(f"Created: {plant1.show()}")
    print(f"Created: {plant2.show()}")
    print(f"Created: {plant3.show()}")
    print(f"Created: {plant4.show()}")
    print(f"Created: {plant5.show()}")

if __name__ == "__main__":
    ft_plant_factory()