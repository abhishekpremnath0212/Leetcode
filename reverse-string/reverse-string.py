class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range((j+1)//2):
            s[i],s[j]=s[j],s[i]
            j-=1
           
        
        
