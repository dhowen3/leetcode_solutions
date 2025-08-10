class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        while True: # run until no changes are made
            new_arr = []
            n = len(intervals)
            i = 0
            while i < n:
                new_elt = intervals[i].copy()
                j = i + 1
                while j < n and  intervals[i][1] >= intervals[j][0]:
                    new_elt[1] = max(intervals[j][1], new_elt[1])
                    j += 1
                new_arr.append(new_elt)
                i = j
            if len(new_arr) == len(intervals):
                break
            else:
                intervals = new_arr
        return intervals
