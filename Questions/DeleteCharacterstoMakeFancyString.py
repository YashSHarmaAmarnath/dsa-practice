class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 1
        count = 1
        while i<n:
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            if count<3:
                ans.append(s[i-1])
            i+=1
        ans.append(s[-1])
        return ''.join(ans)
