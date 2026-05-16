#!/usr/bin/env python3

import sys


def save_data(lines: list[str]) -> None:
    """Save the data with the # (hashtag) at the end of the line"""
    new_file = None
    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "" or " " in new_filename:
        print("Not saving data")
        return
    else:
        try:
            new_file = open(new_filename, 'w')
            print(f"Saving data to '{new_filename}'")
            for line in lines:
                new_file.write(line)
        except Exception as e:
            print(f"Error saving data: {e}\n")
        finally:
            if new_file:
                print(f"Data saved in file '{new_filename}'\n")
                new_file.close()


def process_data(original_lines: list[str]) -> None:
    """Transform lines adding the # (hashtag) symbol at the end of the line"""
    transformed_lines: list[str] = []

    try:
        print("\nTransform data:")
        print("---\n")
        for line in original_lines:
            clean_line = line.rstrip("\n")
            new_line = f"{clean_line}#\n"
            print(new_line, end="")
            transformed_lines.append(new_line)
        print("\n---")
        save_data(transformed_lines)
    except Exception as e:
        print(f"Error processing data: {e}")


def main(filename: str) -> None:
    content = None

    print(f"Accessing file '{filename}'")
    try:
        content = open(filename, 'r')
        lines = content.readlines()
        print("---\n")
        for line in lines:
            new_line = line.rstrip("\n")
            print(new_line)
        print("\n---")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}\n")
    finally:
        if content:
            print(f"File '{filename}' closed.")
            content.close()
            process_data(lines)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)

    print("=== Cyber Archives Recovery ===")
    main(filename=sys.argv[1])
