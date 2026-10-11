import heapq

# new added: 
# kth largest is min val in min heap of size k



class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.heap = nums

        # min heap, smallest at top
        heapq.heapify(self.heap)

        # pop smallest value while there's more elements in heap than k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # left with a heap of size k with the smallest value on top, which is k from largest value
            
        

    def add(self, val: int) -> int:
        
        # insert the value regardless, into heap
        heapq.heappush(self.heap, val)

        # pop the smallest value, since size of heap is 1 more than k
        # left with the smallest value of the k largest, which is the kth largest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
