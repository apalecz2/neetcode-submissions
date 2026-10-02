import heapq

from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        # counter
        # heap by count
        # run sim using queue for timeout, move back to heap once ready

        # just store a count of the steps it takes to empty heap and queue

        if n == 0:
            return len(tasks)

        ctr = [0] * 26

        for t in tasks:
            ctr[ord(t) - ord('A')] -= 1 # subtract for max heap
        
        heap = [count for count in ctr if count < 0]

        heapq.heapify(heap)

        step_count = 0

        # the queue can just be init with n flag values so
        # the next value out is the next task with cooldown expired
        timeout = deque()

        while heap or timeout:

            step_count += 1

            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    timeout.append([count, step_count + n])
            
            if timeout and timeout[0][1] == step_count:
                heapq.heappush(heap, timeout.popleft()[0])


        return step_count

        
