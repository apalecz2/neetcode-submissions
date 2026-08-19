# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# We need at least O(n) to look at all nodes
# So storing all the nodes in a hashmap and reassembling would do this in O(n) time 
# just at the expense of O(n) space

# is there a way to do this without a hashmap?

# pointers?

# I could turn it into a doubly linked list, but that also needs O(n) space for linking back

# 

# left pointer at the start that moves forward 1 after each insert from end, until n/2

# get front half and back half using fast and slow ptrs
# reverse back, insert alternating to merge them






class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now slow points at midpoint

        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse starting at l2

        last = None

        while l2:
            nxt = l2.next

            l2.next = last

            last = l2

            l2 = nxt
        
        l2 = last
        


        while l1 and l2:

            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2

            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2
        









        