class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=itemgetter(0))
        for val in range(len(intervals)-1):
            if intervals[val][1]>intervals[val+1][0]:
                return False
        return True
            
        