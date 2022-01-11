class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        seen={}
        minsum=float("inf")
        ans=[]
        for i in range(len(list1)):
            seen[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in seen:
                if i+seen[list2[i]]==minsum:
                    ans.append(list2[i])
                elif i+seen[list2[i]]<minsum:
                    minsum=i+seen[list2[i]]
                    ans=[list2[i]]
        return ans
                            
                            
            
        