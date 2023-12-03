"""Day 2."""
from pydantic import BaseModel


class Game(BaseModel):
    """
    A single game created from a line in the input.

    Attribues:
        id: game id
        colors: dictionary containing colors mapped to highest value seen among turns.

    """

    # Doesn't need to be a pydantic schema, I wanted to use validators but changed my mind
    id: int
    colors: dict = {"red": 0, "blue": 0, "green": 0}

    def add_turn(self, turn: dict[str, int]) -> None:
        """Add info for a single turn."""
        for key, value in turn.items():
            self.colors[key] = max([self.colors[key], value])

    def check_possible(self, possible: dict[str, int]) -> int:
        """Check if the game was possible given a dict of cube info."""
        for key, value in self.colors.items():
            # check for key error
            if possible[key] < value:
                return 0
        return self.id

    def get_power(self) -> int:
        """Get power for game which is max cubes seen among all turns multiplied."""
        return self.colors["red"] * self.colors["blue"] * self.colors["green"]


def parse_id(row: str) -> tuple[str, str]:
    """Parse and return id and rest of string."""
    row_list = row.split(":")
    game_id = row_list[0]
    game_id = game_id.split(" ")[-1]
    return game_id, row_list[1]


def parse_turn(turn: str) -> dict[str, int]:
    """Parse a single turn."""
    current = {}
    l_cubes = turn.split(", ")
    for color in l_cubes:
        c = color.split(" ")
        current[c[1]] = int(c[0])
    return current


def parse_game(row: str) -> Game:
    """Parse a single line of text and return Game class."""
    game_id, rest_of_str = parse_id(row)
    game = Game(id=game_id)

    game_turns = rest_of_str.split(";")
    for t in game_turns:
        turn = parse_turn(t.strip())
        game.add_turn(turn)

    return game
