class Day2CorruptionChecksum:
    @staticmethod
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

    @staticmethod
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
