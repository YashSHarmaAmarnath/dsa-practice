#****
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(u):
            while parent[u]!=u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u,v):
            u_ = find(u)
            v_ = find(v)
            if u_ == v_:
                return False
            parent[v_] = u_
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []
