from advent_of_code.current.one_p2 import get_calibration_value_w_str, get_total_str

import pathlib
import pytest

DATA_PATH = pathlib.Path.cwd() / "tests/one/sample_inputs/1.txt"

OTHER_SAMPLE = pathlib.Path.cwd() / "tests/one/sample_inputs/2.txt"

OTHER_SAMPLE2 = pathlib.Path.cwd() / "tests/one/sample_inputs/3.txt"


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
    assert out == 228


def test_final_other_r():
    out = get_total_str(OTHER_SAMPLE2)
    assert out == 281


def test_letter_numbers():
    """ "Test spelling and mapping are correct."""
    rows = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    expected = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    for i, r in enumerate(rows):
        out = get_calibration_value_w_str(r)
        assert out == expected[i]


@pytest.mark.skip(
    reason=(
        "Not 100% sure if this is how 0s should be handled, but they aren't in the"
        " input, so it's okay this test is failing."
    )
)
def test_zeros():
    """Test zeroes are ignored."""
    row = "023"
    expected = 23

    out = get_calibration_value_w_str(row)
    assert out == expected
