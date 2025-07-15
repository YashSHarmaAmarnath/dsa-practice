class Solution:
    def isValid(self, word: str) -> bool:
        # wordSet = set(word)
        all_chars = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
}
        nums = {'0','1','2','3','4','5','6','7','8','9'}
        vov,con = 0,0
        if len(word)<3:return False
        for c in word:
            if c not in all_chars and c not in nums:return False
            if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:vov+=1
            elif c not in nums:con+=1
        return False if vov==0 or con==0 else True
        
