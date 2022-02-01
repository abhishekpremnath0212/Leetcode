class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort=sorted(heights)
        c=0
        for i in range(len(heights)):
            if sort[i]!=heights[i]:
                c+=1
        return c
        