class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # adj = {}
        # n=0
        # for edge in edges:
        #     if edge[0] not in adj:
        #         n+=1
        #         adj[edge[0]] = 1
        #     else:
        #         adj[edge[0]] +=1
        #     if edge[1] not in adj:
        #         n+=1
        #         adj[edge[1]] = 1
        #     else:
        #         adj[edge[1]] +=1
            
        # for node in adj:
        #     if adj.get(node) == n-1:
        #         return node
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]

