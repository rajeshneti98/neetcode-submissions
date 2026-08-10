class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for num in s:
            if num-1 not in s:
                currLen = 1
                curr = num+1
                while curr in s:
                    currLen+=1
                    curr+=1
                maxLen = max(currLen, maxLen)
        return maxLen