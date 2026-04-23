#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")
        new_data = data.split(",")
        if len(new_data) != 3:
            print("Invalid syntax")
            continue
        tp = []
        for x in new_data:
            try:
                tp.append(float(x.strip()))
            except ValueError as e:
                print(f"Error on parameter '{x}': {e}")
                break
        else:
            return tuple(tp)


def main() -> None:
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x1, y1, z1 = pos1
    distance1 = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {distance1}\n")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    dist_between = round(math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_between}")


if __name__ == "__main__":
    print("=== Game coordinate system ===")
    main()
