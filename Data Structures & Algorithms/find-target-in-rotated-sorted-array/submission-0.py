class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def findPivot():
            low, high = 0, n-1
            while low < high:
                mid = low + (high-low) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low
        def binarySearch(low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        pivot = findPivot()
        if nums[pivot] <=target and nums[n-1] >=target:
            return binarySearch(pivot, n-1)
        return binarySearch(0, pivot-1)
        