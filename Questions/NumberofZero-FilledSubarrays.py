class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        consecutiveZeros = 0
        count = 0
        for i in range(n):
            if nums[i] == 0:
                consecutiveZeros+=1
                count+=consecutiveZeros
            else:
                consecutiveZeros = 0
        return count
        
