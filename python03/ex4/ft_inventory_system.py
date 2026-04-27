#!/usr/bin/env python3

import sys


def check_duplicates(args) -> None:
    keys = [arg.split(':')[0] for arg in args if ':' in arg]

    seen = set()
    duplicates = set()
    for key in keys:
        if key in seen:
            duplicates.add(key)
        seen.add(key)

    for dup in duplicates:
        print(f"Redundant item '{dup}' - discarding")


def main() -> None:
    args: list = sys.argv[1:]
    dict_new: dict = {}
    new_list: list = list()
    items_quantity: int = 0
    max_val = 0
    min_val = 0

    if not args:
        return

    try:
        check_duplicates(args)
        for arg in args:
            if ':' in arg:
                dict_new.update({arg.split(':')[0]: int(arg.split(':')[1])})
                new_list.append(arg.split(':')[0])
            if ':' not in arg:
                print(f"Error - Invalid parameter '{arg}'")
    except ValueError as e:
        print(f"Quantity error for '{arg.split(':')[1]}': {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    print(f"Got inventory: {dict_new}")
    print(f"Item list: {new_list}")
    print(f"Total quantity of the {len(new_list)} items: {items_quantity}")

    max_val = max(dict_new.values())
    winner = [k for k, v in dict_new.items() if v == max_val]
    min_val = min(dict_new.values())
    looser = [k for k, v in dict_new.items() if v == min_val]
    print(f"Item most abundant: {winner} with quantity {max_val}")
    print(f"Item least abundant: {looser} with quantity {min_val}")

    dict_new.update({'magic item': 1})
    print(f"Updated inventory: {dict_new}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
