# Day 5: Print Queue
from collections import defaultdict

def extract_data(data):
    _sep = data.index("")

    rules = defaultdict(set)
    for i in data[:_sep]:
        a, b = map(int, i.split("|"))
        rules[a].add(b)

    updates = [list(map(int, i.split(","))) for i in data[_sep + 1 :]]
    return rules, updates

def is_valid(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True

def fix_update(rules, update):
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = rules[i] & set(update)

    ordered_keys = sorted(filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True)

    return ordered_keys

def part_1(data):
    rules, updates = extract_data(data)
    add_up = 0

    for update in updates:
        if is_valid(rules, update):
            add_up += update[len(update) // 2]

    return add_up

def part_2(data):
    rules, updates = extract_data(data)
    add_up = 0

    for update in updates:
        if not is_valid(rules, update):
            fixed_update = fix_update(rules, update)
            add_up += fixed_update[len(update) // 2]

    return add_up

def main():
    with open('input.txt', 'r') as file:
        text = file.read().strip().splitlines()

    print(f'Part 1: {part_1(text)}')
    print(f'Part 2: {part_2(text)}')

if __name__ == "__main__":
    main()
