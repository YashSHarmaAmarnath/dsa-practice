class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binSearch(target,l,r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return False
        l,r = 0,len(nums)-1
        while l < r and nums[l] == nums[r]:
            l += 1
        pivote = l
        for i in range(l,r):
            if nums[i]>nums[i+1]:
                pivote = i
                break
        # if pivote == 0:return True if binSearch(target,0,len(nums)-1) else False
        # if nums[0]<=target:return True if binSearch(target,0,pivote-1) else False
        # return True if binSearch(target,pivote+1,len(nums)+1) else False
        if nums[l]<=target<=nums[pivote]:
            return binSearch(target,l,pivote)
        return binSearch(target,pivote+1,r)
