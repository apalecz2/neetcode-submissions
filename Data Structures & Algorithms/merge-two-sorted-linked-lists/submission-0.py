# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Alternate next head of either list, whichever is smaller to be added next

# Can be done in place

# 1. While there is list1 or list2 (either head is not None)
# 2. Get value of both (or one if we've reach the end of one)
# 3. Compare
# 4. Update the pointers based on what should be next




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        head = None

        # Base cases
        if list1 and list2:
            # Initialize head at the smaller of the first nodes, move to next of that list
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        elif list1 and not list2:
            # If no list2 exists, list1 is already sorted and is the final sorted list
            return list1
        elif list2 and not list1:
            # Vice versa
            return list2
        
        
        last = head

        # Until both lists point to None
        while list1 or list2:

            if list1 == None:
                # Just append the rest of list2

                while list2:

                    this = list2 

                    last.next = this

                    last = this

                    list2 = list2.next

                return head
            
            if list2 == None:
                # Append the rest of list1

                while list1:

                    this = list1 

                    last.next = this

                    last = this

                    list1 = list1.next


                return head

            
            # Now we know we still have a node at both

            if list1.val < list2.val:

                # Append the node from list1 since it's smaller
                this = list1 

                last.next = this

                last = this

                list1 = list1.next

            

            else:
                # Append from list2

                this = list2 

                last.next = this

                last = this

                list2 = list2.next
        
        # Now both lists are exhausted and point to None

        
        return head
















