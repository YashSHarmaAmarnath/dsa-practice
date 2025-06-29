class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        fromSet = set([n[0] for n in edges])
        toSet = set([n[1] for n in edges])
        return list(fromSet-toSet)
