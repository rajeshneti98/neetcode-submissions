class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        suffix = 1
        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix*=nums[i]
        for i in range(n-1, -1, -1):
            res[i]*=suffix
            suffix*=nums[i]
        return res
        