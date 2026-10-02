import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # O(n) to process all points into distances
        # then heapify with tuple - dist as [0]
        # want smallest distances
        # so min heap of size k

        # build heap as the dist are calc = O(nlogk)
        # since the height is at most k

        # vs O(n) to process and build heap, then to pop out the n-k other 
        # you'd need nlogk still


        for i in range(len(points)):
            p = points[i]
            d = math.sqrt(p[0]**2 + p[1]**2)
            points[i] = (-d, p)
        
        heapq.heapify(points)

        # max heap so heappop removes larger distance values first
        while points and len(points) > k:
            heapq.heappop(points)
        
        return [p[1] for p in points]