class Solution:
    
    def reverse(self, x: int) -> int:
        if int(str(abs(x))[::-1]) >= pow(2, 31):
            return 0

        if x < 0:
            return -int(str(-x)[::-1])

        return int(str(x)[::-1])