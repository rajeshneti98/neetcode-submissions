class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        buckets = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            buckets[val].append(key)
        res = []
        for item in reversed(buckets):
            if len(res) == k:
                break
            for num in item:
                res.append(num)
        return res