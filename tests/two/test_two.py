from advent_of_code.current.two.utils import parse_id, parse_turn, parse_game, Game
from advent_of_code.current.two.part_one import get_total

import pathlib

ROW = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

POSSIBLE = {"red": 12, "blue": 14, "green": 13}
DATA_PATH = pathlib.Path.cwd() / "tests/two/sample_inputs/1.txt"

def test_parse_id():
    id, rest_of_str = parse_id(ROW)
    assert "1" == id
    assert " 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" == rest_of_str

def test_turn():
    turn = "3 blue, 4 red, 1 green"
    out = parse_turn(turn)

    expected = {
        "red": 4,
        "green": 1,
        "blue": 3
    }

    assert out == expected


def test_parse_game():
    g = parse_game(ROW)

    assert isinstance(g, Game)
    assert g.colors["blue"] == 6
    assert g.colors["red"] == 4
    assert g.colors["green"] == 2

def test_get_total():
    exp_total = 8

    total = get_total(file_path=DATA_PATH, possible=POSSIBLE)

    assert total == exp_total

