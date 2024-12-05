# Day 4: Ceres Search

def part_1(data):
    lines = list(data)
    lines.extend(["".join(row[i] for row in data) for i in range(len(data[0]))])

    def find_diagonals(grid):
        rows, cols = len(grid), len(grid[0])
        main_diagonals, anti_diagonals = {}, {}

        for r in range(rows):
            for c in range(cols):
                main_key, anti_key = r - c, r + c

                main_diagonals.setdefault(main_key, []).append(grid[r][c])
                anti_diagonals.setdefault(anti_key, []).append(grid[r][c])

        return main_diagonals, anti_diagonals

    main_diagonals, anti_diagonals = find_diagonals(data)
    lines.extend("".join(chars) for chars in main_diagonals.values())
    lines.extend("".join(chars) for chars in anti_diagonals.values())

    return sum(line.count("XMAS") + line.count("SAMX") for line in lines)

def part_2(data):
    rows, cols = len(data), len(data[0])
    count = 0
    _set = {"M", "S"}

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if ({data[r - 1][c - 1], data[r + 1][c + 1]} == _set and 
                    {data[r - 1][c + 1], data[r + 1][c - 1]} == _set):
                    count += 1
    return count

def main():
    with open('input.txt', 'r') as file:
        text = file.read().strip().splitlines()

    print(f'Part 1: {part_1(text)}')
    print(f'Part 2: {part_2(text)}')

if __name__ == "__main__":
    main()

