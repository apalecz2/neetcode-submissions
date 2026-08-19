# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # Fast ptr, slow pointer

        #next.next

        #next
        
        # if they don't match, and slow hasn't reached the end yet, continue
        # if slow reaches a node with None, there is no cycle since before it reached it, fast would've equaled it by then

        if head == None or head.next == None:
            return False
        
        fast = head.next
        slow = head

        while fast != slow:

            if slow.next == None:
                return False # slow reached the end without touching fast, no cycle

            if fast and fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False # fast has reached a natural end

            
            slow = slow.next
        
        # Fast has pointed to the same as slow, there must be a cycle

        return True
        



