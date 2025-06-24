class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        numProvinces = 0
        visited = [False]*n
        def dfs(i):
            for j in range(n):
                if not visited[j]  and isConnected[i][j] == 1:
                    visited[j] = True
                    dfs(j)
                    
                
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                numProvinces+=1
        return numProvinces
