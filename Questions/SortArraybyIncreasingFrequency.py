class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        nums.sort()
        length = len(numSet)
        frequency = [[0,n] for n in numSet]
        hashMap = {frequency[i][1]:i for i in range(length)}
        for n in nums:
            frequency[hashMap[n]][0]+=1
        frequency.sort(key=lambda x:(x[0],-x[1]))
        # for i in range(length-1):
        #     if frequency[i][0] == frequency[i+1][0] and frequency[i][1] < frequency[i+1][1]:
        #         frequency[i][1],frequency[i+1][1] = frequency[i+1][1],frequency[i][1]  
        res = []
        for f,n in frequency:
            res.extend([n]*f)
        return res
            
