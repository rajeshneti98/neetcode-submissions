class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(s):
            sum = 0
            for pile in piles:
                sum += math.ceil(pile/s)
            return sum <=h
        low, high = 1, max(piles)
        res = high
        while low <=high:
            mid = low + (high-low) // 2
            if isPossible(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
        