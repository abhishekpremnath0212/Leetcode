class Solution:
    def convertToBase7(self, num: int) -> str:
        abs_num = abs(num)
        val = ''
        ans = ''
        while abs_num >= 7:
            val += str(abs_num % 7)
            abs_num = abs_num // 7
        val += str(abs_num % 7) 
        val = val[::-1]
        if num < 0: 
            ans = '-'
        ans += val
        return ans