class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsum=max(nums)
        maxc,minc=1,1
        for i in range(len(nums)):
            tmp=maxc
            maxc=max(maxc*nums[i],minc*nums[i],nums[i])
            minc=min(tmp*nums[i],minc*nums[i],nums[i])
            maxsum=max(maxsum,maxc)
        return maxsum
        
                
        
        