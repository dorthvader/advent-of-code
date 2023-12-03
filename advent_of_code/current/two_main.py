"""Script to get total for part 1 of the question."""
# pylint: disable=R0801
import csv
import pathlib

from advent_of_code.current.two import parse_game

INPUT_PATH = pathlib.Path.cwd() / "advent_of_code/current/inputs/two.txt"

POSSIBLE = {"red": 12, "blue": 14, "green": 13}


def get_total(file_path: pathlib.Path, possible: dict[str, int]) -> int:
    """
    Get total.

    Determine which games would have been possible if the bag had been loaded with only 12 red cubes
    13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
    """

    with open(file_path, newline="", mode="r", encoding="utf-8") as csvfile:
        line_reader = csv.reader(csvfile, delimiter="\n")

        total = 0

        for row in line_reader:
            g = parse_game(row[0])
            total += g.check_possible(possible=possible)

    return total


if __name__ == "__main__":
    print(get_total(file_path=INPUT_PATH, possible=POSSIBLE))
