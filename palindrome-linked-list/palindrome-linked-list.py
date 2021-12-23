# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p2=head 
        p5=head
        l=0
        while p5 and p5.next:
            p5=p5.next.next
            p2=p2.next
            l+=1
        
        p1=None
        while p2 is not None:
            p3=p2.next
            p2.next=p1
            p1=p2
            p2=p3
        
        p0=head
        while p1 and p0:
            if p0.val != p1.val:
                return False
            p0=p0.next
            p1=p1.next
        return True
            
        
        
        
        
            
            
        