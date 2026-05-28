#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = 'r',
        content: str = "") -> tuple[bool, str]:
    success: bool = False
    tp: tuple[bool, str] = tuple()

    try:
        success = True
        if (action == 'w'):
            with open(filename, action) as file:
                file.write(content)
                tp = (success, "Content successfully written to file")
        else:
            with open(filename, action) as file:
                content = file.read()
                tp = (success, str(content))
    except (FileNotFoundError, PermissionError) as error:
        success = False
        tp = (success, str(error))
    return (tp)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/non/existingfile'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient.txt'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('ancient2.txt', 'w', 'holaaaaaa'))
