class MedianFinder:

    def __init__(self):
        # self.n = 0
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.small)<len(self.large):
            heapq.heappush(self.small,-heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return float(-self.small[0])
        else:
            return float(-self.small[0]+self.large[0])/2.0





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
