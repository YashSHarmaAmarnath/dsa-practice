class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the
        # elements from index i to j-1. Can we use this property to optimize it.
        n  = len(nums)
        hashMap = {}
        hashMap[0] = 1
        curSum = 0
        count = 0
        for i in range(n):
            curSum+=nums[i]
            if curSum-k in hashMap:
                count += hashMap[curSum-k]
            if curSum in hashMap:
                hashMap[curSum]+=1
            else:
                hashMap[curSum]=1
        
        return count
