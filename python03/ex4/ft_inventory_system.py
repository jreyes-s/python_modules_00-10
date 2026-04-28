#!/usr/bin/env python3

import sys


def check_duplicates(args: list) -> None:
    keys = [arg.split(':')[0] for arg in args if ':' in arg]

    seen = set()
    duplicates = set()
    for key in keys:
        if key in seen:
            duplicates.add(key)
        seen.add(key)

    for dup in duplicates:
        print(f"Redundant item '{dup}' - discarding")


def percentage(dict_new: dict, quantity: int) -> None:
    for k, v in dict_new.items():
        percent = round((v * 100) / quantity, 1)
        print(f"Item {k} presents {percent}%")


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
                key, value_str = arg.split(':')
                value = int(value_str)

                if key not in dict_new:
                    dict_new[key] = value
                    new_list.append(arg.split(':')[0])
            if ':' not in arg:
                print(f"Error - Invalid parameter '{arg}'")
    except ValueError as e:
        print(f"Quantity error for '{arg.split(':')[0]}': {e}")
    except IndexError as e:
        print(f"IndexError: {e}")

    print(f"Got inventory: {dict_new}")
    print(f"Item list: {new_list}")

    items_quantity = sum(dict_new.values())
    print(f"Total quantity of the {len(dict_new)} items: {items_quantity}")

    percentage(dict_new, items_quantity)

    winner = max(dict_new, key=dict_new.get)
    max_val = dict_new[winner]
    loser = min(dict_new, key=dict_new.get)
    min_val = dict_new[loser]
    print(f"Item most abundant: {winner} with quantity {max_val}")
    print(f"Item least abundant: {loser} with quantity {min_val}")

    dict_new.update({'magic item': 1})
    print(f"Updated inventory: {dict_new}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
