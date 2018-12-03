import itertools


class Day2InventoryManagementSystem:

    @staticmethod
    def solve1(ids):
        count_2 = 0
        count_3 = 0
        for current_id in ids:
            char_cache = dict()
            for char in current_id:
                char_cache[char] = char_cache.get(char) + 1 if char in char_cache else 1
            # another way would be to iterate and check if one with 2 and one with 3 exists which
            # also would be a bit more efficient but this approach is nicer to
            counts = set(char_cache.items())
            count_2 = count_2 + 1 if 2 in counts else count_2
            count_3 = count_3 + 1 if 3 in counts else count_3
        return count_2 * count_3

    @staticmethod
    def solve2(ids):
        matching = None
        for id1, id2 in itertools.combinations(ids, 2):
            has_mismatch = False
            for i, (c1, c2) in enumerate(zip(id1, id2)):
                if c1 is not c2:
                    if has_mismatch:
                        matching = None
                        break
                    matching = id1[:i] + id1[i + 1:]
                    has_mismatch = True
            if matching:
                break
        return matching

        # don't like this approach due to excessive string concat
        # common_characters = ""
        # for id1, id2 in itertools.combinations(ids, 2):
        #     has_mismatch = False
        #     for c1, c2 in zip(id1, id2):
        #         if c1 is c2:
        #             common_characters += c1
        #         else:
        #             if has_mismatch:
        #                 common_characters = ""
        #                 break
        #             has_mismatch = True
        #     if common_characters:
        #         break
        # return common_characters.strip()
