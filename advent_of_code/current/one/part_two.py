import csv
import pathlib

INPUT_PATH = pathlib.Path.cwd() / "advent_of_code/current/inputs/one.txt"

STR_NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SOLID_STR_NUMS = "one two three four five six seven eight nine"
STR_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_total_str(file_path: pathlib.Path = INPUT_PATH) -> int:
    with open(file_path, newline="", mode="r") as csvfile:
        line_reader = csv.reader(csvfile)
        total = 0
        for row in line_reader:
            total += get_calibration_value_w_str(row[0])
        return total


def get_calibration_value_w_str(line: str) -> int:
    line = line.lower()
    left_num, right_num = None, None

    left_stash = ""
    right_stash = ""

    left = 0
    right = -1
    while left_num is None or right_num is None:
        if left == len(line):
            return 0
        if line[left].isdigit() and left_num is None:
            left_num = line[left]
        elif left_num is None:
            left_stash += line[left]
            if left_stash in SOLID_STR_NUMS:
                if left_stash in STR_NUMS:
                    left_num = STR_MAPPING[left_stash]
            else:
                new_stash = ""
                for l in left_stash[::-1]:
                    if l + new_stash in SOLID_STR_NUMS:
                        new_stash = l + new_stash
                    else:
                        break

                left_stash = new_stash

        if line[right].isdigit() and right_num is None:
            right_num = line[right]
        elif right_num is None:
            right_stash = line[right] + right_stash
            if right_stash in SOLID_STR_NUMS:
                if right_stash in STR_NUMS:
                    right_num = STR_MAPPING[right_stash]
            else:
                new_stash = ""
                for l in right_stash:
                    if new_stash + l in SOLID_STR_NUMS:
                        new_stash += l
                    else:
                        break
                right_stash = new_stash

        left += 1
        right -= 1
    return int(left_num + right_num)


if __name__ == "__main__":
    out = get_total_str()
    print(out)
