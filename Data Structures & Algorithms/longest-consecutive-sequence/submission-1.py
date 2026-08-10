class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        s = set(nums)
        maxLength = 1
        for num in nums:
            if num-1 not in s:
                currLength = 1
                curr = num
                while curr+1 in s:
                    curr = curr+1
                    currLength+=1
                maxLength = max(maxLength, currLength)
        return maxLength