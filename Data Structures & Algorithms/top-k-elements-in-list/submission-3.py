class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        li = sorted(count.items(), key = lambda x: x[1], reverse = True)[0:k]
        res = [item[0] for item in li]
        return res