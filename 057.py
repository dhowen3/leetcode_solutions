class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for interval in intervals:
            if interval[0] <= newInterval[0] and interval[1] >= newInterval[1]:
                newInterval = interval
            elif newInterval[0] <= interval[1] and interval[1] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
            elif interval[0] <= newInterval[1] and newInterval[1] <= interval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                new_intervals.append(interval)
        new_intervals.append(newInterval)
        return sorted(new_intervals, key=lambda x: x[0])
