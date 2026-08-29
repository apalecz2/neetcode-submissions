
# just sounds like a tree
# I guess priority queues can be trees
# Tree satisfies logn insert, 1 midpoint retrieval 
# -> split tree on midpoint - root is median



class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        
        if not self.small and not self.large:
            heapq.heappush(self.small, -num)
            return
        
        if num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # balance
        if len(self.small) > len(self.large) + 1:
            popped = -heapq.heappop(self.small)
            heapq.heappush(self.large, popped)
        elif len(self.large) > len(self.small) + 1:
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0
        