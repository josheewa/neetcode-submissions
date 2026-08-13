class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pmap = {i:[] for i in range(numCourses)}
        visiting = set()
        for crs, pre in prerequisites:
            pmap[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting: return False
            if pmap[crs] == []: return True

            visiting.add(crs)
            for pre in pmap[crs]:
                if not dfs(pre): return False
            
            visiting.remove(crs)
            pmap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True