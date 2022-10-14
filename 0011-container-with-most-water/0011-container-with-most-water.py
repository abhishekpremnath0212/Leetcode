class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        ans=0
        r=len(height)-1
        while l<r:
            area=(r-l)*min(height[l],height[r])
            # print(area)
            # break
            ans=max(area,ans)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return ans
        
        
            
        