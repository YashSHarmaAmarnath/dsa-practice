class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        mx = -1
        for k in count:
            if k == count.get(k):
                mx = max(k,mx)
        return mx
