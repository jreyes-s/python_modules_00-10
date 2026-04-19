#!/usr/bin/env python3

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existing/file", "r")
    elif operation_number == 3:
        _ = "hello" + 123
    else:
        return


def test_error_type() -> None:
    print("=== Garden Error types demo ===")

    for i in range(0, 3):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_type()
