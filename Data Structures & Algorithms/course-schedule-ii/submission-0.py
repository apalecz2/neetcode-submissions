
# spanning tree along the edges
# potentially union find on merging the semi complete paths
# brute force is make the mapping of course to prereq, dfs or bfs until all used
# need to start search from each course,??, or sort to find starting course??
# sort by what?

# any course with rank 0 can be a starting node of dfs
# then once that course has been taken, the surrounding nodes all are less 1 in rank,
# continue to any next nodes with 0 rank

# continue until a valid sequence is found


# 1. Process to get a list mapping and rank of each course to prereqs

# 2. 

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build adjacency list

        c_to_pr = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for c, pr in prerequisites:
            c_to_pr[pr].append(c)
            in_degree[c] += 1
        
        # bfs starting at all courses with length 0 pr lists
        q = deque([])

        out = []

        # add all courses that can be taken right away to the queue
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)


        while q:

            current_course = q.popleft()

            out.append(current_course)

            for dep in c_to_pr[current_course]:
                in_degree[dep] -= 1

                if in_degree[dep] == 0:
                    q.append(dep)
        
            
        if len(out) == numCourses:
            return out
        else:
            return []











        