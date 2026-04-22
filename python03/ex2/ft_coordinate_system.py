#!/usr/bin/env python3

import math

def get_player_pos() -> tuple[float, ...]:
	while True:
		data = input("Enter new coordinates as floats in format 'x,y,z': ")
		new_data = data.split(",")
		if len(new_data) != 3:
			print("Invalid syntax")
			get_player_pos()
		tp = []
		for x in new_data:
			try:
				tp.append(float(x.strip()))
			except ValueError as e:
				print(f"Error on parameter '{x}: {e}")
				break
		else:
			return tuple(tp)


def main() -> None:
	player_pos = get_player_pos()
	x, y, z = player_pos
	print((x, y, z))


if __name__ == "__main__":
	print("=== Game coordinate system ===")
	print("\nGet a first set of coordinates")
	main()
