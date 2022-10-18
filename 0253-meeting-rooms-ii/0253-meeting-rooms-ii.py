
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))
        minheap=[]
        heapq.heappush(minheap,intervals[0][1])
        for i in range(1,len(intervals)):
            if intervals[i][0]>=minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap,intervals[i][1])
        return len(minheap)
        
        
        