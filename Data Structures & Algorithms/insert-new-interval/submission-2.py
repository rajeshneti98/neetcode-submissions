class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end, mid = 0, len(intervals)-1, 0
        while(start<=end):
            mid = start + (end-start)//2
            interval = intervals[mid]
            if interval[0] < newInterval[0]:
                start = mid+1
            else:
                end  = mid-1
        intervals.insert(start, newInterval)
        prev = intervals[0]
        res = []
        for curr in intervals[1:]:
            if curr[0]<=prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(prev)
                prev = curr
        res.append(prev)
        return res

        