class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda pair: pair[0])
        [start1, end1] = intervals[0]
        for [start2, end2] in intervals[1:]:
            if start2<=end1:
                start1 = min(start1, start2)
                end1 = max(end1, end2)
            else:
                # print(start1, end1)
                res.append([start1, end1])
                start1 = start2
                end1 = end2
        # print(start1, end1) 
        res.append([start1, end1])
        return res            
        