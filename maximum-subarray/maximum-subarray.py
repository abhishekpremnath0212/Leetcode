class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxc,maxf=nums[0],nums[0]
        for i in range(1,len(nums)):
            maxc=max(maxc+nums[i],nums[i])
            maxf=(max(maxc,maxf))
        return maxf
        