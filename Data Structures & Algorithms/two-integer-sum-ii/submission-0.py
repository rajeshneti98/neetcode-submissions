class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        s = {}
        for i in range(n):
            diff = target - numbers[i]
            if diff in s:
                return [s[diff],i+1]
            s[numbers[i]] = i+1
        return []
        