class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxDif=0
        for n in nums:
            if n+1 in count:
                maxDif=max(maxDif,count[n]+count[n+1])
        return maxDif
