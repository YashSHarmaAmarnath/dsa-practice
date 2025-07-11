class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        charset = set(s)
        for c in charset:
            # counter = {}
            # maxf= 0
            # for j in range(i,n):
            #     counter[s[j]] = 1+counter.get(s[j],0)
            #     maxf = max(maxf,counter[s[j]])
            #     if (j-i+1) - maxf <= k:
            #         res = max(res,j-i+1)
            count = 0
            l = 0
            for r in range(n):
                if s[r] == c:
                    count+=1
                while (r-l+1)-count>k:
                    if s[l] == c:
                        count-=1
                    l+=1
                res = max(res,r-l+1)
        return res
