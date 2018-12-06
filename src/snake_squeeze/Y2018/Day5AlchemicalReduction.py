import re

COLLUSION_DIFF = 32


class Day5AlchemicalReduction:
    @staticmethod
    def solve1(test):
        i = 1
        while i < len(test):
            if abs(ord(test[i]) - ord(test[i - 1])) == COLLUSION_DIFF:
                test = test[:i - 1] + test[i + 1:]
                i -= 1
            else:
                i += 1
        return len(test.strip())

    def solve2(self, test):
        result = len(test)
        for i in range(65, 91):
            remove = "[{}]".format(str(chr(i) + chr(i + COLLUSION_DIFF)))
            tmp = re.sub(remove, '', test)
            result = min(result, self.solve1(tmp))
        return result
