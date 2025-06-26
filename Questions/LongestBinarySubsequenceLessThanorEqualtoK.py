class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n=len(s)
#rint(n)
        if n== 0:
            if k == int(s,2):
                return 1
            else:
                return 0
        curr = ""
        ci=0
        for i in range(n-1,-1,-1):
        
            if int(s[i:n],2)>k:
                break
            ci = i
        cnt0 = 0
        #print(ci)
        for i in range(ci):
            if s[i]  == "0":
                cnt0+=1
        return cnt0+(n-ci)
