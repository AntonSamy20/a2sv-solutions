# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even = ListNode(-1,None)
        start_even = even
        
        curr = head.next
        while curr:
            
            even.next = curr.next

            curr.val = curr.next.val 
            curr.next = curr.next.next        