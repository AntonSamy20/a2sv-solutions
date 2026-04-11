# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        mx = 0
        while prev:
            mx = max(head.val + prev.val ,mx)

            head = head.next
            prev = prev.next

        return mx

        
        