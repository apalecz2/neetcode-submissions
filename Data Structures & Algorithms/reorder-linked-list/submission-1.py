# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        if not head or not head.next:
            return



        # reverse the second half
        # interweave

        # 1. Reverse second half

        # 1.a Get midpoint
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Now slow is the node before the middle node

        # Reverse
        second = slow.next
        slow.next = None
        

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt



        # Interweave
        # Two heads of lists
        l1, l2 = head, prev


        while l2:

            nxt1, nxt2 = l1.next, l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2


            


















