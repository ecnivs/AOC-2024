# Day 2: Red-Nosed reports

def is_sequence_safe(levels):
    increasing = all(levels[i+1] - levels[i] >= 1 and levels[i+1] - levels[i] <= 3 
        for i in range(len(levels)-1))
    decreasing = all(levels[i] - levels[i+1] >= 1 and levels[i] - levels[i+1] <= 3 
        for i in range(len(levels)-1))
    return increasing or decreasing

def is_report_safe(levels, use_problem_dampener=False):
    if is_sequence_safe(levels):
        return True

    if not use_problem_dampener:
        return False

    for i in range(len(levels)):
        reduced_levels = levels[:i] + levels[i+1:]

        if is_sequence_safe(reduced_levels):
            return True
    return False

def parse_input(input_file):
    with open(input_file, 'r') as f:
        return [list(map(int, line.split())) for line in f]

def solve_part1(reports):
    return sum(1 for report in reports if is_report_safe(report, use_problem_dampener=False))

def solve_part2(reports):
    return sum(1 for report in reports if is_report_safe(report, use_problem_dampener=True))

def main():
    input_file = 'input.txt'
    reports = parse_input(input_file)

    safe_reports_part1 = solve_part1(reports)
    print(f'Part 1: {safe_reports_part1}')

    safe_reports_part2 = solve_part2(reports)
    print(f'Part 2: {safe_reports_part2}')

if __name__ == "__main__":
    main()
