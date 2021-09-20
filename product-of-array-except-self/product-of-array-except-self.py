class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[None]*l
        ans[0]=1
        for i in range(1,l):
            ans[i]=ans[i-1]*nums[i-1]#all numbers to the left of the number
        
        p=1#using a variable instead of another list
        for i in range(l-1,-1,-1):
            ans[i]=ans[i]*p#all numbers to the right of the number
            p=p*nums[i]
        
        return ans
        