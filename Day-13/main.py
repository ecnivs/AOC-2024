# Day 13: Claw Contraption
from __future__ import annotations
import re
from pathlib import Path
from typing import ParamSpec, TypeAlias, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

Pair: TypeAlias = tuple[int, int]
Button = Pair
Prize = Pair
GameInfo: TypeAlias = dict[Prize, tuple[Button, Button]]

REGEX = (
    r"Button A: X\+(\d+), Y\+(\d+)\s*"
    r"Button B: X\+(\d+), Y\+(\d+)\s*"
    r"Prize: X=(\d+), Y=(\d+)"
)

PART2_OFFSET = 10_000_000_000_000

def get_data() -> GameInfo:
    with Path("./input.txt").open() as file:
        data = file.read()

    matches = re.findall(REGEX, data)

    return {
        (int(match[4]), int(match[5])): (
            (int(match[0]), int(match[1])),
            (int(match[2]), int(match[3])),
        )
        for match in matches
    }

def play_claw_machine(prize: Prize, button_a: Button, button_b: Button):
    prize_x, prize_y = prize
    a_x, a_y = button_a
    b_x, b_y = button_b

    D = a_x * b_y - a_y * b_x
    if D == 0:
        return None

    D_a = prize_x * b_y - prize_y * b_x
    D_b = a_x * prize_y - a_y * prize_x

    if D_a % D != 0 or D_b % D != 0:
        return None

    count_a = D_a // D
    count_b = D_b // D

    if count_a < 0 or count_b < 0:
        return None

    return count_a * 3 + count_b

def part1(data: GameInfo) -> int:
    total_tokens = 0

    for prize, (button_a, button_b) in data.items():
        min_cost = play_claw_machine(prize, button_a, button_b)
        if min_cost is not None:
            total_tokens += min_cost

    return total_tokens

def part2(data: GameInfo) -> int:
    total_tokens = 0

    data = {
        (prize_x + PART2_OFFSET, prize_y + PART2_OFFSET): buttons
        for (prize_x, prize_y), buttons in data.items()
    }

    for prize, (button_a, button_b) in data.items():
        min_cost = play_claw_machine(prize, button_a, button_b)
        if min_cost is not None:
            total_tokens += min_cost

    return total_tokens

def main():
    data = get_data()

    result1 = part1(data)
    print(f"Part 1: {result1}")

    result2 = part2(data)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
