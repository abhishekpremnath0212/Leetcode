class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeb={'(':')','{':'}','[':']'}
        openb=['{','(','[']
        for b in s:
            if b in openb:
                stack.append(b)
            else:
                if stack and b == closeb[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack==[]
        