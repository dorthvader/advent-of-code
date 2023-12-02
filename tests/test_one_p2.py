from advent_of_code.current.one_p2 import get_calibration_value_w_str, get_total_str

import pathlib

DATA_PATH = pathlib.Path.cwd() / "tests/sample.txt"

OTHER_SAMPLE = pathlib.Path.cwd() / "tests/sample_2.txt"

OTHER_SAMPLE2 = pathlib.Path.cwd() / "tests/sample2.txt"


def test_get_calibration_value_w_str():
    row = "two1nine"
    output = get_calibration_value_w_str(row)
    assert output == 29


def test_get_ints():
    row = "4nineeightseven2"
    output = get_calibration_value_w_str(row)
    assert output == 42


def test_single_int():
    row = "9nnnh"
    output = get_calibration_value_w_str(row)
    assert output == 99


def test_single_word():
    row = "ninennnh"
    output = get_calibration_value_w_str(row)
    assert output == 99


def test_something():
    row = "eigninehhh"
    output = get_calibration_value_w_str(row)
    assert output == 99


def test_something_else():
    row = "eig7ninehhh"
    output = get_calibration_value_w_str(row)
    assert output == 79


def test_something_else_ale():
    row = "eig7niehhh"
    output = get_calibration_value_w_str(row)
    assert output == 77


def test_something_else_alex():
    row = "78oooofivefiveoooo"
    output = get_calibration_value_w_str(row)
    assert output == 75


def test_final():
    out = get_total_str(DATA_PATH)
    assert out == 285


def test_final_other():
    out = get_total_str(OTHER_SAMPLE)
    assert out == 281


def test_final_other_r():
    out = get_total_str(OTHER_SAMPLE2)
    assert out == 228
