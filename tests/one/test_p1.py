from advent_of_code.current.one.part_one import get_calibration_value, get_total

import pathlib

DATA_PATH = pathlib.Path.cwd() / "tests/one/sample_inputs/1.txt"


def test_get_calibration_values():
    single_line = "kjrqmzv9mmtxhgvsevenhvq7"
    output = get_calibration_value(single_line)
    assert output == 97


def test_get_calibration_values_many_ints():
    single_line = "2two3seven9rshkhrjzlv2"
    output = get_calibration_value(single_line)
    assert output == 22


def test_final():
    out = get_total(DATA_PATH)
    assert out == 281
