# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Instinct is to: iterate through each list, grab head, compare
# Comparisons could be tough -> k comparisons -> finding min of next is the challenge

# How do we maintain minumum of next vals?


# O(n * k) is just compare / search all heads for min val
# then append that node

# divide + conquer
# merge 2, then merge 2 of those ...

# how to split?
# how to merge?

# while lists len > 0
# 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None


        # Loop until all lists are exhausted
        while len(lists) > 1:

            merged_lists = []

            # Pick 2 lists, merge, head of new list goes in the first spot, other is popped

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i+1 >= len(lists):
                    merged_lists.append(list1)
                    continue
                list2 = lists[i+1]

                merged = self.mergeTwoLists(list1, list2)
                merged_lists.append(merged)
            
            lists = merged_lists
        
        return lists[0] # just 1 list remains
            





            
        
        

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
        







