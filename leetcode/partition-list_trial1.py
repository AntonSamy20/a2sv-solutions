# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        start_small = small
        big = ListNode(0)
        start_big = big

        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else :
                big.next = curr
                big = big.next
            
            curr = curr.next

        big.next = None
        small.next = start_big.next

        return start_small.next


        


        