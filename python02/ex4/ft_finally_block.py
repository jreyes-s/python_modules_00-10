#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
        return


def test_watering_system(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")
