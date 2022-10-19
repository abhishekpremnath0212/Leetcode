class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted(interval[0] for interval in intervals )
        end=sorted(interval[1] for interval in intervals )
        s=0
        e=0
        ans=0
        while s<len(intervals):
            if start[s]>=end[e]:
                ans-=1
                e+=1
            ans+=1
            s+=1
        return ans