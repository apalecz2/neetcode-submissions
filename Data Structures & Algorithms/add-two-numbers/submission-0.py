# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# reverse each, then add like in math class by digit with carry

# gives O(1) space, O(n) time

# sum needs to be a linked list. So just as we do the addition make a node and connect it up




class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        last_added = dummy

        carry = 0
        # while there is still both nodes to add, add both
        while l1 or l2:

            # add a node with the sum of the vals at these nodes, and the carry if any
            v1, v2 = 0, 0

            if l1: v1 = l1.val
            if l2: v2 = l2.val

            total = v1 + v2 + carry

            this_digit = 0
            if total > 9:
                # could mod here, lets just do strings
                carry = int(str(total)[0])
                this_digit = int(str(total)[1])
            else:
                carry = 0
                this_digit = total

            curr_sum_node = ListNode(this_digit)

            # now link the node
            last_added.next = curr_sum_node
            last_added = curr_sum_node

            # move the lists forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            carry_node = ListNode(carry)
            last_added.next = carry_node

        return dummy.next
































        