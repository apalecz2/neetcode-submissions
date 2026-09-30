import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        # sort, then binary search to get the intervals that include query, check for shortest out of them

        # b search until q greater than left_i, less than right_i, then step in each direction and hold min_length
        # until both can't meet the criteria

        # nlogn

        # heap? on length, traverse down while q in length
        # same / similar to above


        intervals.sort()
        o_queries = queries[:]
        queries.sort()

        min_heap = []
        q_to_shortest = {}
        i = 0

        for q in queries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                q_to_shortest[q] = min_heap[0][0]
            else:
                q_to_shortest[q] = -1
        
        return [q_to_shortest[q] for q in o_queries]

                







