#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    t_int = int(temp_str)

    if t_int < 0:
        raise ValueError(f"{t_int}°C is too cold for plants (min. 0°C)")
    elif t_int > 40:
        raise ValueError(f"{t_int}°C is too hot for plants (max. 40°C)")
    return t_int


def test_temperature(temp_str) -> None:
    print("=== Garden Temperature Checker ===")
    for data in temp_str:
        print(f"\nInput data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature(["25", "abc", "100", "-50"])
