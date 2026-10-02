import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(n) build heap, pop smallest each time a new value is found 
        # larger than the [0] value in the min heap
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):

            v = nums[i]

            # add to heap if larger than smallest
            if v > heap[0]:
                heapq.heappushpop(heap, v)
            
            # otherwise skip this value, since it's smaller
        
        return heap[0]
        

            


