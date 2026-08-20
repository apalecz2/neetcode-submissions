# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# How can we do this?
# O(n) since we need to know length

# Fast ptr slow ptr, 

# Binary search with fp sp? to get to the n desired?

# Cut in half with fpsp, if n < fp.len


# This is O(1) space, since we just need pointers for slow and fast
# Then we can start at head if n in head, slow, or start at slow if n in slow, fast
# loop until we find it.

# Still O(n) time, since we need to process all nodes to get the total length
# But instead of a couple more passes in full, to

# Wait
# Why not 2 passes? If it has to be O(n) to know length, why not just make a counter, and determine the node to delete
# then walk to it again using a step counter, and update ptrs to remove it?





class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        dummy.next = head

        fast = dummy
        slow = dummy

        while fast.next:

            if n > 0:
                fast = fast.next
                n -= 1
            else:
                # Advance both
                fast = fast.next
                slow = slow.next

        
        # Now we have fast at the final node

        # And slow n nodes behind it at the node to be removed

        # Update ptr:
        slow.next = slow.next.next
        
        return dummy.next










