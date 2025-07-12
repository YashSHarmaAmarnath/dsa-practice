class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:return not s
        firstmatch = bool(s) and (s[0]==p[0] or p[0]==".")
        if len(p)>=2 and p[1] == "*":
            return self.isMatch(s,p[2:]) or (firstmatch and self.isMatch(s[1:],p))
        else:
            return firstmatch and self.isMatch(s[1:],p[1:])
