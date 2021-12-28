class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        for i in array:
            val=abs(i)
            if array[val-1]<0:
                return val
            array[val-1]*=-1
		
    
        