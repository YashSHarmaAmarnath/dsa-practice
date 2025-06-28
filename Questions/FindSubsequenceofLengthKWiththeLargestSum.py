class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        newnums = []
        for i in range(len(nums)):
            newnums.append([nums[i],i])
        newnums.sort(reverse=True)
        ans = [0]*k
        newnums = sorted(newnums[:k],key=lambda x: x[1])
        for i in range(k):
            ans[i] = newnums[i][0]
        return ans
