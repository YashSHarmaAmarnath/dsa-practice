class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap = []
        n = len(startTime)
        gap = [startTime[0]]
        for i in range(1,n):
                gap.append(startTime[i]-endTime[i-1])
        gap.append(eventTime-endTime[-1])
        curr = sum(gap[:k+1])
        mx = curr
        for i in range(k+1,n+1):
            curr += gap[i] - gap[i-k-1]
            mx = max(curr,mx)
        return mx
