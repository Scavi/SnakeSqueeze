class Day1InverseCaptcha:
    @staticmethod
    def solve(number, is_adjacent: bool = True):
        result = 0
        split = 1
        if not is_adjacent:
            split = int(len(number) / 2)

        for i, val in enumerate(number):
            if number[i] == number[(i + split) % len(number)]:
                result += int(number[i])
        return result
