"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # O(n) is definitely achievable
        # no hashmap?

        # walk the list, make a copy list,
        # then walk a second time, and just link to the new randoms?
        # but how to get the randoms without a map?
        # can i add another property to the original map that has the new random node?
        # then just copy that?

        if not head:
            return None

        dummy = Node(0)
        prev = dummy

        rand_map = {}

        curr = head

        while curr:
            copy = Node(curr.val)

            rand_map[curr] = copy

            prev.next = copy
            prev = copy

            curr = curr.next

        # now copy of list exists starting at dummy.next
        # with next and val set, but not rand

        curr = head
        while curr:
            rand_map[curr].next = rand_map.get(curr.next)
            rand_map[curr].random = rand_map.get(curr.random)
            curr = curr.next

    

        return dummy.next