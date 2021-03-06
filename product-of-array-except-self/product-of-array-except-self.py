class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[None]*l
        ans[0]=1
        for i in range(1,l):
            ans[i]=nums[i-1]*ans[i-1]
        tmp=1
        for i in range(l-1,-1,-1):
            ans[i]=ans[i]*tmp
            tmp=tmp*nums[i]
        return ans