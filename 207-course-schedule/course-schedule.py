class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = {i:[] for i in range(numCourses)}
        for cor, pre in prerequisites:
            preqs[cor].append(pre)
        
        visited_courses = set()
        def dfs(crs):
            if crs in visited_courses:
                return False
            if preqs[crs] == []:
                return True
            
            visited_courses.add(crs)
            for pre in preqs[crs]:
                if not dfs(pre):
                    return False
            visited_courses.remove(crs)
            preqs[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True