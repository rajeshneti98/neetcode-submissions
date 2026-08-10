class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return n
        nums = sorted(nums)
        maxLength = 1
        currLength = 1
        curr = nums[0]
        for i in range(1,n):
            if nums[i] == (curr+1):
                currLength+=1
                curr = nums[i]
                maxLength = max(maxLength, currLength)
            elif nums[i] == curr:
                continue
            else:
                curr = nums[i]
                currLength = 1
        return maxLength
        