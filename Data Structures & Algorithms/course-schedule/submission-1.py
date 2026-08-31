
# this can be thought of as a graph
# dependency graph
# cycle detection?
# it's directed graph, need to check if it's acyclical

# DAG


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        course_to_prer = {i: [] for i in range(numCourses)}
        
        for prerequisite in prerequisites:
            a, b = prerequisite
            course_to_prer[a].append(b)
        
        def dfs(course, ctp, visited):

            if not visited:
                visited = set()
                visited.add(course)
            else:
                if course in visited:
                    return False
                visited.add(course)
            

            for r in ctp[course]:
                if not dfs(r, ctp, visited):
                    return False
            

            
            
            visited.remove(course)

            ctp[course] = []

            return True
            

        
        for course in course_to_prer.keys():
            
            if not dfs(course, course_to_prer, None):
                return False
        
        return True


            


