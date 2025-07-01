class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        count = 1
        i = 0
        while i<n-1:
            if word[i] == word[i+1]:
                count+=1
            i+=1
        return count
