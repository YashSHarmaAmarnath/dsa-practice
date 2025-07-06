class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.n2 = len(nums2)
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val+val
        self.cnt2[old_val]-=1
        self.cnt2[new_val]+=1
        if self.cnt2[old_val]==0:
            del self.cnt2[old_val]
        if 0<=index<self.n2:
            self.nums2[index] += val

    def count(self, tot: int) -> int:
        count = 0
        for n in self.cnt1:
            count += self.cnt1[n]*self.cnt2.get(tot-n,0) 
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
