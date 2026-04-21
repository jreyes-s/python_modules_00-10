#!/usr/bin/env python3

import sys

def ft_score_analytics(score: list) -> None:
    total_players: int = len(score)
    total_score: int = sum(score)
    average_score: float = total_score / total_players
    high_score: int = max(score)
    low_score: int = min(score)
    score_range: int = high_score - low_score

    print(f"Scores processed: {score}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")
    print("\n")


def main() -> None:
    if len(sys.argv) == 1:
        print("No score provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
        return

    clean_scores = []    
    for i in sys.argv[1:]:
        try:
            clean_scores += [int(i)]
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    if not clean_scores:
        print("No score provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
    else:
        ft_score_analytics(clean_scores)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
