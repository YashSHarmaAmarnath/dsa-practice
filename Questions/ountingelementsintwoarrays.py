class Solution:
    def countLessEq(self, a, b):
        # code here
        # n = len(a)
        # m = len(b) 
        # ans = [0]*n
        # for i in range(n):
        #     count = 0
        #     for j in range(m):
        #         if a[i]>=b[j]:
        #             count+=1
        #     ans[i] = count
        # return ans
        n = len(a)
        m = len(b) 
        b.sort()
        def binSearch(n):
            l,r = 0,m-1
            while l<=r:
                mid = l + (r-l) //2
                if b[mid] <= n:
                    l = mid+1
                else:
                    r = mid-1
            return l
        ans = [0]*n
        for i in range(n):
            ans[i] = binSearch(a[i])
        return ans
