class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(1))
        pend=intervals[0][1]
        c=0
        for start,end in intervals[1:]:
            if start>=pend:
                pend=end
            else:
                c+=1
                pend=min(pend,end)
        return c
        