class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])
      
        s,e,c,mc=0,0,0,0
        while s<len(start):
            if start[s]<end[e]:
                c+=1
                s+=1
            else:
                c-=1
                e+=1
            mc=max(mc,c)
        return mc
           