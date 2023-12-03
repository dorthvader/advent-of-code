import csv
import pathlib

INPUT_PATH = pathlib.Path.cwd() / "advent_of_code/current/inputs/one.txt"


def get_total(file_path: pathlib.Path = INPUT_PATH) -> int:
    with open(file_path, newline="", mode="r") as csvfile:
        line_reader = csv.reader(csvfile)
        total = 0
        for row in line_reader:
            total += get_calibration_value(row[0])
        return total


def get_calibration_value(line: str) -> int:
    left_num, right_num = None, None
    left = 0
    right = -1
    while left_num is None or right_num is None:
        if left == len(line):
            return 0
        if line[left].isdigit() and left_num is None:
            left_num = line[left]
        if line[right].isdigit() and right_num is None:
            right_num = line[right]
        left += 1
        right -= 1
    return int(left_num + right_num)
