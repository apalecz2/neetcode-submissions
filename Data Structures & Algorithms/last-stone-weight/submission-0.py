
# max heap - O(n) first run

# pop 2 - O(1)

# smash and insert = logn or 1

# happens O(n) times
# so nlogn, but i feel like something cancels out since we reuse the heap and are 
# decreasing what we're incremementing over??

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)

        # there are 2 stones to smash
        while heap and len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 == stone2:
                continue
            else:
                # 1 is larger
                larger = max(stone1, stone2)
                smaller = min(stone1, stone2)

                # opposite for max heap
                new = smaller - larger

                heapq.heappush(heap, new)
        
        # now 0 or 1 stones remain
        if heap:
            return -heap[0]
        else:
            return 0


        