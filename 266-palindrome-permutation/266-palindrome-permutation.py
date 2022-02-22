class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        else:
            # count frequency of chars
            count_dict = {}
            for i in s:
                count_dict[i] = count_dict.get(i,0)+1
            
            # at most, we could have one odd number in frequency
            count_odd=0
            for v in count_dict.values():
                if v%2 !=0 and count_odd==0:
                    count_odd+=1
                elif v%2 !=0 and count_odd>=1:
                    return False
            return True