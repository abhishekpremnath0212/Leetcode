class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        last = 0
        while left <= right:
            middle = left+(right-left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
                last = 1
            else:
                right = middle - 1
                last = 0
        if last == 0:
            return left
        else:
            return left