

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # get list length
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        # calculate target (from start)
        target = length - n + 1
        
        # account for edge case: remove first node
        if target == 1:
            return head.next
        
        # remove target node
        length = 0
        curr = head
        while curr:
            length += 1
            if length == target:
                prev.next = curr.next
                
            prev, curr = curr, curr.next
            
        return head