class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0]*(n+1)
        res[1] = 1
        def count1(num):
            count = 0
            while num:
                count += num%2
                num //=2
            return count

        for i in range(2,n+1):
            res[i] = count1(i)
        return res
