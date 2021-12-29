class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort=sorted(intervals,key=lambda x:x[0])
        ans=[]
        ans.append(sort[0])	
        for i in range(1,len(sort)):
            if ans[-1][1]>=sort[i][0]:
                ans[-1][1]=max(ans[-1][1],sort[i][1])
            else:
                ans.append(sort[i])
        return ans