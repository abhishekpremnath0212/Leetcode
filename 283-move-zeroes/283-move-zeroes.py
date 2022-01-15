class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[r]=nums[i]
                r+=1
        for i in range(r,len(nums)):
            nums[i]=0 
        