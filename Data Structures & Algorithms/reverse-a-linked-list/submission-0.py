# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # just reverse the ptr at each node
        # return the last node as head

        # node.next = last, None if first

        last = None

        while head:
            
            # Update last for the next iter
            nxt = head.next

            # Update this nodes next ptr
            head.next = last

            last = head
            
            # Move to the next node, (None if last)
            head = nxt

        # return head which is now last

        return last

            




        