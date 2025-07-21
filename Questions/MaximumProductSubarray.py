class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,maxPro,curMin = nums[0],nums[0],nums[0]
        for i in nums[1:]:
            temp = max(curMax*i,i,curMin*i)
            curMin = min(curMax*i,i,curMin*i)
            curMax = temp
            maxPro = max(maxPro,curMax)
        return maxPro
