


# dfs from each water cell, add to sets for each, then intersection



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        def dfs(x, y, prev_h, visit_set):

            
            if (x, y) in visit_set:
                return
            
            this_height = heights[x][y]

            if this_height == "#":
                return

            # only walk upwards or equal
            if this_height < prev_h:
                return

            visit_set.add((x, y))


            if x > 0: dfs(x - 1, y, this_height, visit_set)
            if x < (len(heights) - 1): dfs(x + 1, y, this_height, visit_set)
            if y > 0: dfs(x, y - 1, this_height, visit_set)
            if y < (len(heights[0]) - 1): dfs(x, y + 1, this_height, visit_set)

        

        reach_by_a = set()
        reach_by_p = set()

        for i in range(len(heights)):
            # left side, j constant at 0
            dfs(i, 0, float('-inf'), reach_by_p) # from p

            # right side, j at length
            dfs(i, len(heights[0]) - 1, float('-inf'), reach_by_a) # from a

        for j in range(len(heights[0])):
            # top with i constant at 0
            dfs(0, j, float('-inf'), reach_by_p) # from p

            # bottom i at length
            dfs(len(heights) - 1, j, float('-inf'), reach_by_a) # from a
        
        return [list(coord) for coord in reach_by_a.intersection(reach_by_p)]

        
        






