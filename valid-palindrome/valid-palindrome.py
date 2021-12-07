class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=[]
        for i in s:
            if i.isalnum():
                j.append(i.lower())
        if j==j[::-1]:
            return True
        return False
            
            



        