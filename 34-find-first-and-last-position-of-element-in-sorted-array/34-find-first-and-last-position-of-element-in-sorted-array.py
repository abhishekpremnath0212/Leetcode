class Solution:
    def search(self,nums,target,leftvalue):
        l,r=0,len(nums)-1
        i=-1
        
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                i=mid
                if leftvalue:
                    r=mid-1
                else:
                    l=mid+1
        return i
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.search(nums,target,True)
        b=self.search(nums,target,False)
        return [a,b]
        