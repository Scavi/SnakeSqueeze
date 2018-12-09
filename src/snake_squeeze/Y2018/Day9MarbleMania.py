import collections
import re


class Day9MarbleMania:

    def __init__(self, game_data, marble_multiplier=1):
        self._player_count = int(re.search("^[^\\s]*", game_data).group(0))
        self._last_marble = int(re.search("(?<=(worth\\s))[^\\s]*", game_data).group(0)) * marble_multiplier
        self._marble_list = collections.deque()
        self._marble_list.append(0)
        self._scores = dict()


    def solve(self):
        max_score = 0
        for m in range(1, self._last_marble + 1):
            if m % 23 == 0:
                self._marble_list.rotate(7)
                max_score = max(max_score, self._add_score(m, self._marble_list.pop()))
                self._marble_list.rotate(-1)
            else:
                self._marble_list.rotate(-1)
                self._marble_list.append(m)
        return max_score


    def _add_score(self, marble, value):
        player = (marble % self._player_count + 1)
        if player not in self._scores:
            self._scores[player] = 0
        self._scores[player] = marble + value + self._scores[player]
        # print("Player {} has the new score {}".format(player, self._scores[player]))
        return self._scores[player]
