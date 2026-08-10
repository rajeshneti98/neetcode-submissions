class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        res = []
        while i<n:
            j, k = i+1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j<n-1 and nums[j] == nums[j+1]:
                        j+=1
                    while k>0 and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1                    
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -=1
                else:
                    j +=1
            while i<n-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res