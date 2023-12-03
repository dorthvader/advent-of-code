"""Script to get total for part 2 of the question."""
# pylint: disable=R0801
import csv
import pathlib

from advent_of_code.current.two import parse_game

INPUT_PATH = pathlib.Path.cwd() / "advent_of_code/current/inputs/two.txt"


def get_total_power(file_path: pathlib.Path) -> int:
    """
    Get total.

    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    with open(file_path, newline="", mode="r", encoding="utf-8") as csvfile:
        line_reader = csv.reader(csvfile, delimiter="\n")

        total = 0

        for row in line_reader:
            g = parse_game(row[0])
            total += g.get_power()

    return total


if __name__ == "__main__":
    print(get_total_power(file_path=INPUT_PATH))
