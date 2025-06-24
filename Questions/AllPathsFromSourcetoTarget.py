class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [False]*n
        def backTrack(i):
            if visited[i]: return 
            if i == n-1: return [[i]]
            visited[i] = True
            ans = []
            for v in graph[i]:
                p2 = backTrack(v)
                if p2:
                    for p in p2:
                        ans.append([i]+p)
            visited[i] = False
            return ans
        return backTrack(0)

