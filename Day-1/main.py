# Day 1: Historian Hysteria

def part_one(left, right):
    total = 0
    left = sorted(left)
    right = sorted(right)
    total = sum(abs(l - r) for l, r in zip(left, right))
    return total

def part_two(left, right):
    total = 0
    for i in left:
        total += i * right.count(i)
    return total

def main():
    left, right = [], []
    with open('input.txt', 'r') as txt:
        for line in txt.readlines():
            x, y = (int(value) for value in line.split())
            left.append(x)
            right.append(y)

    print(f'Part 1: {part_one(left, right)}')
    print(f'Part 2: {part_two(left, right)}')

if __name__ == "__main__":
    main()
