import re
from array import array
from datetime import datetime
from datetime import timedelta

ID_PATTERN = "(?<=\\#)[^\\s]*"
DATE_TIME_PATTERN = "(?<=\\[)[^\\]]*"


class Day4ReposeRecord:
    def solve(self, guard_records):
        list.sort(guard_records)
        guard_log = dict()
        current_guard = None
        most_sleepy_guard = None
        predictable_guard = None
        for i in range(0, len(guard_records)):
            if "begins shift" in guard_records[i]:
                current_guard = self._determine_guard(guard_records[i], guard_log)
            else:
                current_guard.add(guard_records[i])
            if i == 0:
                most_sleepy_guard = current_guard
                predictable_guard = current_guard
            else:
                most_sleepy_guard = most_sleepy_guard.who_is_more_sleepy(current_guard)
                predictable_guard = predictable_guard.who_is_more_predictable(current_guard)
        return most_sleepy_guard.guard_id * most_sleepy_guard.slept_max_at, \
               predictable_guard.guard_id * predictable_guard.slept_max_at

    @staticmethod
    def _determine_guard(record, guard_log):
        lookup = re.search(ID_PATTERN, record)
        if not lookup:
            raise ValueError("Illegal guard ID in '{}'!".format(record))
        guard_id = int(lookup.group(0))
        if guard_id in guard_log:
            guard = guard_log.get(guard_id)
        else:
            guard = _Guard(guard_id, record)
            guard_log[guard_id] = guard
        return guard


class _Guard:
    SHIFT_MINUTES = 60

    def __init__(self, guard_id, record):
        self.guard_id = guard_id
        self.is_awake = True
        self.date_time = self._extract_date(record)
        self.shift = array('i', (0 for _ in range(0, _Guard.SHIFT_MINUTES)))
        self.slept_max_at = 0
        self.overall_sleep_time = 0

    def add(self, record):
        date_change = self._extract_date(record)
        # falls asleep
        if self.is_awake:
            self.is_awake = False
            self.date_time = date_change
        else:
            for i in range(self.date_time.minute, date_change.minute):
                self.overall_sleep_time += 1
                self.shift[i] += 1
                if self.shift[self.slept_max_at] < self.shift[i]:
                    self.slept_max_at = i
            self.is_awake = True

    def who_is_more_sleepy(self, guard):
        return guard if guard.overall_sleep_time > self.overall_sleep_time else self

    def who_is_more_predictable(self, guard):
        return guard if guard.shift[guard.slept_max_at] > self.shift[guard.slept_max_at] else self

    @staticmethod
    def _extract_date(record):
        date_time_lookup = re.search(DATE_TIME_PATTERN, record)
        if not date_time_lookup:
            raise ValueError("Illegal date time format in '{}'".format(record))
        date_time = datetime.strptime(date_time_lookup.group(0), "%Y-%m-%d %H:%M")
        if date_time.hour is 23:
            date_time = date_time + timedelta(minutes=60 - date_time.minute)
        return date_time
