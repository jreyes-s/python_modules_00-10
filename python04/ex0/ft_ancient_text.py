#!/usr/bin/env python3

import sys


def main(file_name: str) -> None:
    content = None

    print(f"Accessing file '{file_name}'")
    try:
        content = open(file_name, 'r')
        print("---\n")
        print(content.read(), end="")
        print("\n---")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}\n")
    finally:
        if content:
            content.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)

    print("=== Cyber Archives Recovery ===")
    main(file_name=sys.argv[1])
