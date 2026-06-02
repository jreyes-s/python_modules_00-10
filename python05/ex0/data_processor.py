#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """ Esta es una clase de prueba """

    def __init__(self):
        self._stored_data: List[str] = []
        self._processed_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """ Verfica si los datos de entrada son apropiados para este procesador. """
        pass

    def ingest(self, data: Any) -> None:
        """ Procesa y almacena los datos de entrada. """
        if not self.validate(data):
            raise ValueError(
                f"Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._stored_data.append(str(item))
        else:
            self._stored_data.append(str(data))

    def output(self) -> tuple[int, str]:
        """ Extrae el dato más antiguo almacenado y su rango de procesamiento. """
        if not self._stored_data:
            raise IndexError("No data available.")

        oldest_data = self._stored_data.pop(0)
        self._processed_count += 1

        return (self._processed_count, oldest_data)


class NumericProcessor(DataProcessor):
    _valid_types = (int, bool)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and data:
            return all(isinstance(item, self._valid_types) for item in data)
        if isinstance(data, self._valid_types):
            return True
        return False


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and data:
            return all(isinstance(item, str) for item in data)
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def _is_valid_log(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        return (
            "log_level" in data and isinstance(data["log_level"], str) and
            "log_message" in data and isinstance(data["log_message"], str)
        )

    def validate(self, data: Any) -> bool:
        # 4. Corregido: Implementamos la validación usando el método existente
        if self._is_valid_log(data):
            return True
        if isinstance(data, dict) and data:
            return all(self._is_valid_log(data) for k, v in data)
        return False

    def ingest(self, data: Any):
        print("Ingesttttt")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # ------------------------------------------
    # 1. Pruebas de NumericProcessor
    # ------------------------------------------
    print("\nTesting Numeric Processor...")
    numeric_proc = NumericProcessor()

    print(f" Trying to validate input '42': {numeric_proc.validate(42)}")
    print(
        f" Trying to validate input 'Hello': {numeric_proc.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_proc.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f" Got exception: {e}")

    num_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    numeric_proc.ingest(num_data)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = numeric_proc.output()
        print(f" Numeric value {rank}: {val}")

    # ------------------------------------------
    # 2. Pruebas de TextProcessor
    # ------------------------------------------
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()

    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    # ------------------------------------------
    # 3. Pruebas de LogProcessor
    # ------------------------------------------
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
