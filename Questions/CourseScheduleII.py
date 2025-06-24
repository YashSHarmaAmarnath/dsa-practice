class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        recStack = set()
        visited = set()
        adj = {}
        stack = []

        for d,s in prerequisites:
            if s in adj:
                adj[s].add(d)
            else:
                adj[s] = {d}
        # print(adj)
        def checkCycle(i):
            if i in recStack:return True
            if i in visited:return False
            recStack.add(i)
            visited.add(i)

            for neighbor in adj.get(i,[]):
                if checkCycle(neighbor):
                    return True
            recStack.remove(i)
            return False
        
        for n in range(numCourses):
            if n not in visited:
                if checkCycle(n):
                    return stack
        visited.clear()
        def dfs(curr):
            visited.add(curr)
            for nebor in adj.get(curr,[]):
                if nebor not in visited:
                    dfs(nebor)
            stack.append(curr)
        for node in range(numCourses):
            if node not in visited:
                dfs(node)
        return stack[::-1]
        
