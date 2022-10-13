class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans=1
        cans=1
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==1+nums[i-1]:
                    cans+=1
                else:
                    ans=max(ans,cans)
                    cans=1
        return max(ans,cans)
        
            
            
        
        