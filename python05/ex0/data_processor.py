#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """ Esta es una clase de prueba """
    @abstractmethod
    def validate(self, data: Any) -> bool:
        print("Validate")

    @abstractmethod
    def ingest(self, data: Any) -> None:
        print("Ingest")

    def output(self) -> tuple[int, str]:
        print("Ingest Data")


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


def main() -> None:
    print("This is a test")


if __name__ == "__main__":
    main()
