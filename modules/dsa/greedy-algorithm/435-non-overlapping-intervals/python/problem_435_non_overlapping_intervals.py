from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]
        for start, finish in intervals[1:]:
            if start >= end:
                count += 1
                end = finish
        return len(intervals) - count
