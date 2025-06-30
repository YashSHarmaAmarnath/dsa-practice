class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        n = len(stones)
        while n>1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            if s1 == s2:
                n-=2
            else:
                heapq.heappush(stones,-(s1-s2))
                n-=1
        return -heapq.heappop(stones) if stones else 0
