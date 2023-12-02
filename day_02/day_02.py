import re
from typing import Dict, List


def get_clean_input() -> List[List[Dict[str, int]]]:
    clean_input = []
    with open("./day_02/day_02.txt") as f:
        lines = f.readlines()

    for line in lines:
        games = [game for game in line.split(";")]

        clean_games = []

        for game in games:
            game_dict = dict()
            for color in game.split(","):
                value = re.findall(r"\d+", color)
                if "red" in color:
                    game_dict.update({"red": int(value[-1])})
                elif "blue" in color:
                    game_dict.update({"blue": int(value[-1])})
                elif "green" in color:
                    game_dict.update({"green": int(value[-1])})

                clean_games.append(game_dict)

        clean_input.append(clean_games)

    return clean_input


def part_a() -> None:
    games = get_clean_input()
    sum_ids = 0

    for id, game in enumerate(games):
        is_game_valid = True
        for turn in game:
            if (
                turn.get("red", 0) > 12
                or turn.get("green", 0) > 13
                or turn.get("blue", 0) > 14
            ):
                is_game_valid = False
                break

        if is_game_valid:
            sum_ids += id + 1

    print(sum_ids)


def part_b() -> None:
    games = get_clean_input()

    overall_power = 0

    for game in games:
        min_red, min_blue, min_green = [1] * 3

        for turn in game:
            min_red = max(min_red, turn.get("red", 0))
            min_blue = max(min_blue, turn.get("blue", 0))
            min_green = max(min_green, turn.get("green", 0))

        power = min_red * min_blue * min_green

        overall_power += power

    print(overall_power)


if __name__ == "__main__":
    part_a()
    part_b()
