from pathlib import Path

from Util.FileHelper import FileHelper


def solve_a(file_lines):
    result = 0
    for i, line in enumerate(file_lines):
        line_tokens = line.split()

        min_value = 10000000
        max_value = 0
        for j, token in enumerate(line_tokens):
            min_value = min(int(token), min_value)
            max_value = max(int(token), max_value)

        result += max_value - min_value
    return result


def solve_b(file_lines):
    result = 0
    for y, line in enumerate(file_lines):
        line_tokens = line.split()
        for x in range(1, len(line_tokens)):
            for i in range(x):
                min_value = min(int(line_tokens[i]), int(line_tokens[x]))
                max_value = max(int(line_tokens[i]), int(line_tokens[x]))

                if max_value % min_value == 0:
                    result += max_value // min_value
    return result



# Question 1
puzzle_input = FileHelper.read_file(Path("../Input/Day2.txt"))
res1 = solve_a(puzzle_input)
print(str(res1))


# Question 2
test = ["5\t9\t2\t8", "9\t4\t7\t3", "3\t8\t6\t5"]

r = solve_b(test)
res2 = solve_b(puzzle_input)
print(str(res2))