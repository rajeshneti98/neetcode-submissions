class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num]+=1
        li = sorted(map.items(), key = lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(li[i][0])
        return res