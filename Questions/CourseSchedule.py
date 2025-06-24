class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        recStack = set()
        adj = {}
        for d,s in prerequisites:
            if s in adj:
                adj[s].add(d)
            else:
                adj[s] ={d}
        
        def dfs(n):
            if n in recStack:return True
            if n in visited:return False
            recStack.add(n)
            visited.add(n)

            for v in adj.get(n,[]):
                    if dfs(v):
                        return True
            recStack.remove(n)
            return False

        for n in adj:
            if dfs(n):
                return False
        return True
