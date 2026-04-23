#!/usr/bin/env python3

class GardenError(Exception):
    """Exception base for the garden"""

    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_problem() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_problem() -> None:
    raise WaterError("Not enougth water in the tank!")


def test_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print(f"Testing WaterError...")
    try:
        raise_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for action in [raise_plant_problem, raise_water_problem]:
        try:
            action()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
