class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        pirlist = [0]*n
        # 1->even 0->odd
        for i in range(n):
            pirlist[i] = 1 if nums[i]%2==0 else 0 
        first = pirlist[0]
        alt_first = 0 if first==1 else 1

        first_count = 0
        for i in range(n):
            if pirlist[i] == first:first_count+=1
        
        alt_count = 0
        for i in range(n):
            if pirlist[i] == first:
                alt_count+=1
                if first==1:
                    first = 0
                else:
                    first = 1
        
        alt_first_count = 0
        for i in range(n):
            if pirlist[i] == alt_first:alt_first_count+=1


        return max(first_count,alt_count,alt_first_count)


