#!/usr/bin/env python3

class Plant:
    def __init__(self, hola: str) -> None:
        self.hola = hola

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 18:
            return True
        return False

def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")

if __name__ == "__main__":
    ft_garden_analytics()
