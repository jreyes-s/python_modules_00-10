#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("Garden Temperature ===")
    data = ["25", "abc"]

    for d in data:
        print(f"\nInput data is '{d}'")
        try:
            temperature = input_temperature(d)
            print(f"Temperature is now {temperature}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
