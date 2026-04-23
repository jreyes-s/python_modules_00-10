#!/usr/bin/env python3

import random

all_possible_achievements = {
    'Crafting Genius',
    'Strategist',
    'World Savior',
    'Speed Runner',
    'Survivor',
    'Master Explorer',
    'Treasure Hunter',
    'Unstoppable',
    'First Steps',
    'Collector Supreme',
    'Untouchable',
    'Sharp Mind',
    'Boss Slayer',
    'The King',
    'Your Favourite Team mamiii',
    'They Call Me Romeo'
}


def gen_player_achievements(achievement_list: list) -> set:
    num: int = random.randint(1, len(all_possible_achievements))
    selection: list = random.sample(achievement_list, num)

    return (set(selection))


def main() -> None:
    mazo: list = list(all_possible_achievements)
    players: list = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_data: dict = {}

    for player in players:
        players_data[player] = gen_player_achievements(mazo)
        print(f"Player {player}: {players_data[player]}")

    all_distinct: set = set.union(*players_data.values())
    common_achievements: set = set.intersection(*players_data.values())
    print(f"\nAll distinct achievements: {all_distinct}")
    print(f"\nCommon achievements: {common_achievements}\n")

    for p, ach in players_data.items():
        o_ach = set.union(
            *(players_data[name] for name in players_data if name != p))
        print(
            f"Only {p} has: {set.difference(players_data[p], o_ach)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()
