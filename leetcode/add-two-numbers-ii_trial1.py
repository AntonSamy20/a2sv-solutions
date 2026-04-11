# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        st1 = []
        curr = l1
        while curr:
            st1.append(curr.val)
            curr = curr.next

        st2 = []
        curr = l2
        while curr:
            st2.append(curr.val)
            curr = curr.next

        c = 0
        while st1 or st2 or c:
            x = st1.pop() if st1 else 0
            y = st2.pop() if st2 else 0
            tot = x + y + c
            c = tot//10

            new_node = ListNode(tot%10)
            new_node.next = head
            head = new_node

        return head


        