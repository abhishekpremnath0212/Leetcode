# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cn=dummy
        c=0
        while l1 or l2 or c>0:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            node=ListNode((v1+v2+c)%10)
            cn.next=node
            cn=cn.next
            c=(v1+v2+c)//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
            
        