class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval
            if start <= prev_end:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
            prev_end = res[-1][1]
        return res
