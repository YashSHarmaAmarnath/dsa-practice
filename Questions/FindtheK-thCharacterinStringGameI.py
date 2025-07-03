class Solution:
    def kthCharacter(self, k: int) -> str:
        def changer(ch):
            return chr((ord(ch.lower()) - ord('a') + 1) % 26 + ord('a'))
        word = "a"
        n = 1
        while n<k:
            nxt = ""
            for ch in word:
                nxt+=changer(ch)
                n+=1
            word+=nxt
        return word[k-1]
