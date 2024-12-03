# Day 3: Mull It Over
import re

def part_1(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, "".join(data))
    result = sum(int(x) * int(y) for x, y in matches)

    return result

def part_2(string):
    pattern = r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"
    regex = re.compile(pattern)

    result = 0
    enabled = True

    for match in re.finditer(regex, string):
        if match.group(0) == "do()":
            enabled = True
            continue
        if match.group(0) == "don't()":
            enabled = False
            continue
        if enabled:
            numbers = [int(_) for _ in match.group(0)[4:-1].split(",")]
            result += numbers[0] * numbers[1]

    return result

def main():
    with open('input.txt', 'r') as file:
        text = file.read()

    print(f'Part 1: {part_1(text)}')
    print(f'Part 2: {part_2(text)}')

if __name__ == "__main__":
    main()
