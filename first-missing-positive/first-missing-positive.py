class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n or nums[i]-1 == i or nums[i] == nums[nums[i]-1]:
                i+=1
            else:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        for i in range(n):
            if nums[i]-1 != i:
                return i+1
        return n+1