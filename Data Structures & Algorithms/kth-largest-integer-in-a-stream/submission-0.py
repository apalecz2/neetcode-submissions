
# reverse the order, just store the k largest as smallest (negate)
# this means the kth largest is the top of the heap in the now min heap
# for each new value just insert it into this
# init is O(n) to make heap, insert is logn (provided not skewed - which heapq handles)


# in python its automatically a min heap
# to keep the k largest values in a min heap - make it a max heap by negating
# then pop the end of the array after an insert (only 1 needs to come back out)
# 

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.heap = nums
        
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)



    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
