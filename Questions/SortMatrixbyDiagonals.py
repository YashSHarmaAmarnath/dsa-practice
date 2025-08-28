class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonal = {}
        for i in range(n):
            for j in range(n):
                diagonal.setdefault(j-i,[]).append(grid[i][j])

        for k in diagonal.keys():
            if k<=0:
                diagonal[k].sort()
            else:
                diagonal[k].sort(reverse=True)
        
        for i in range(n):
            for j in range(n):
                grid[i][j]=diagonal[j-i].pop()
        return grid
