#!/usr/bin/env python3

import sys


def get_user_input(prompt: str) -> str:
    """ Get the user input using low level streams """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        return ""
    return line.rstrip("\n")


def save_data(lines: list[str]) -> None:
    """Save the data with the # (hashtag) at the end of the line"""
    new_file = None
    new_filename = get_user_input("Enter new file name (or empty): ")
    if new_filename is not None:
        sys.stdout.write(f"Saving data to '{new_filename}'\n")
    if new_filename == "" or " " in new_filename:
        sys.stdout.write("Data not saved.")
        sys.stdout.flush()
        return
    try:
        new_file = open(new_filename, 'w')
        for line in lines:
            new_file.write(line)
            sys.stdout.flush()
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error saving data: {e}\n")
        sys.stderr.flush()
        sys.exit(1)
    finally:
        if new_file:
            sys.stdout.write(f"Data saved in file '{new_filename}'\n")
            sys.stdout.flush()
            new_file.close()
        else:
            sys.stdout.write("Data not saved.")


def process_data(original_lines: list[str]) -> None:
    """Transform lines adding the # (hashtag) symbol at the end of the line"""
    transformed_lines: list[str] = []

    try:
        sys.stdout.write("\nTransform data:\n")
        sys.stdout.write("---\n\n")
        for line in original_lines:
            clean_line = line.rstrip("\n")
            new_line = f"{clean_line}#\n"
            sys.stdout.write(new_line)
            transformed_lines.append(new_line)
        sys.stdout.write("\n---\n")
        sys.stdout.flush()
        save_data(transformed_lines)
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error processing data: {e}")
        sys.stderr.flush()
        sys.exit(1)


def main() -> None:
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        sys.stderr.write("[STDERR] Usage: ft_ancient_text.py <file>\n")
        sys.stderr.flush()
        sys.exit(1)

    content = None
    filename = sys.argv[1]

    sys.stdout.write(f"Accessing file '{filename}'\n")
    sys.stdout.flush()
    try:
        content = open(filename, 'r')
        lines = content.readlines()
        sys.stdout.write("---\n\n")
        sys.stdout.flush()
        for line in lines:
            new_line = line.rstrip("\n")
            sys.stdout.write(f"{new_line}\n")
        sys.stdout.write("\n---\n")
        sys.stdout.flush()
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
    finally:
        if content:
            sys.stdout.write(f"File '{filename}' closed.\n")
            sys.stdout.flush()
            content.close()
            process_data(lines)
    sys.exit(1)


if __name__ == "__main__":
    sys.stdout.write("=== Cyber Archives Recovery ===\n")
    sys.stdout.flush()
    main()
