class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def distance_from_origin(x,y):
        #     return math.sqrt(x**2 + y**2)
        heap = []
        res = []
        for x,y in points:
            dis = x**2 + y**2
            heapq.heappush(heap, (dis, [x, y]))
        for _ in range(k):
                res.append(heapq.heappop(heap)[1])
        # print(hashMap)
        # return hashMap.get(heapq.heappop(heap))
        return res
