class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*(l*2)
        j=l
        for i in range(l):
            ans[i],ans[j]=nums[i],nums[i] 
            j+=1
        return ans
        
    