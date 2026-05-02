#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "Alek", "Mamba", "Mambo", "Clark", "Kent",
        "TheBoss"
    ]

    actions: list[str] = [
        "run", "dance", "climb", "fly", "eat",
        "move", "sleep", "grab", "release"
    ]

    while True:
        yield (random.choice(players), random.choice(actions))

"""
def consume_event() -> Generator[tuple[str, str], None, None]:
"""


def main() -> None:
    events = gen_event()
    lista: list = list()
    try:
        for i in range(1000):
            player_event = next(events)
            player = player_event[0]
            action = player_event[1]
            print(f"Event {i}: Player {player} did action {action}")
        for _ in range(10):
            lista.append(next(events))
    except StopIteration as e:
        print(f"Un problema ocurrio: {e}")
    print(f"Built list of 10 events: {lista}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
