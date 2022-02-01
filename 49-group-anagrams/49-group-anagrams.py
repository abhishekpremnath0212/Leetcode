class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        
        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-97]+=1
            seen[tuple(count)].append(w)
        return seen.values()