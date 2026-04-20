#!/usr/bin/env python3

import sys

def ft_command_quest() -> None:
    length = len(sys.argv)
    if length == 1:
        print("No arguments provided!")
    elif length > 1:
        print(f"Arguments received: {length - 1}")
        for i in range(1, length):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {length}\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    ft_command_quest()
