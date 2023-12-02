"""Test cases provided by dev with working answer."""

from advent_of_code.current.one_p2 import get_calibration_value_w_str, get_total_str

import pathlib


def test_differences():
    expected = 16
    row = "1fouronesixsvhbglmvxx"

    out = get_calibration_value_w_str(row)

    assert out == expected


def test_other_difference():
    expected = 93
    row = "dzttdmpfxtnine6onefourone3vnnz"

    out = get_calibration_value_w_str(row)

    assert out == expected
