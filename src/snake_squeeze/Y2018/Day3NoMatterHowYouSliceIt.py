import re


class Day3NoMatterHowYouSliceIt:
    def __init__(self, fabric_size=10):
        self._fabric_size = fabric_size

    def solve1(self, claims):
        duplicated, _ = self._determine_claims(claims)
        return duplicated

    def solve2(self, claims):
        _, claim_data = self._determine_claims(claims)
        return claim_data.pop()

    def _determine_claims(self, claims):
        duplicated = 0
        claim_data = dict()
        fabric = [[_Inch() for _ in range(self._fabric_size)] for _ in range(self._fabric_size)]
        for claim in claims:
            tokens = [int(x) for x in filter(None, re.split("#|@|,|:|x", claim))]
            for y in range(tokens[1], tokens[1] + tokens[3]):
                for x in range(tokens[2], tokens[2] + tokens[4]):
                    fabric[x][y].count += 1
                    if fabric[x][y].count == 1:
                        fabric[x][y].id = tokens[0]
                        if tokens[0] not in claim_data:
                            claim_data[tokens[0]] = False
                    elif fabric[x][y].count == 2:
                        duplicated += 1
                        claim_data[fabric[x][y].id] = True
                        claim_data[tokens[0]] = True
        return duplicated, {k for k, v in claim_data.items() if not v}


class _Inch:
    id = 0
    count = 0
