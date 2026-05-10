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


def consume_event(lista: list) -> Generator[tuple[str, str], None, None]:
    while lista:
        idx = random.randrange(len(lista))
        event = lista.pop(idx)
        print(f"Got event from list: {event}")
        yield event


def main() -> None:
    events = gen_event()
    lista: list = []
    try:
        for i in range(1000):
            player_event = next(events)
            player = player_event[0]
            action = player_event[1]
            print(f"Event {i}: Player {player} did action {action}")
        for _ in range(10):
            lista.append(next(events))
    except StopIteration as e:
        print({e})
    print(f"Built list of 10 events: {lista}")

    consumer = consume_event(lista)
    for event in consumer:
        print(f"Remains in list: {lista}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
