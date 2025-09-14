class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        hash = {}
        vowel = {'a','e','i','o','u'}
        def vovleEnc(word):
            word = word.lower()
            wl = []
            for w in word:
                if w in vowel:
                    wl.append("*")
                else:
                    wl.append(w)
            return ''.join(wl)

        wordSet = set(wordlist)
        hash1 = {}
        for word in wordlist:
            if word.lower() not in hash:
                hash[word.lower()] = word
            if vovleEnc(word.lower()) not in hash1:
                hash1[vovleEnc(word.lower())] = word

        res = []
        for q in queries:
            if q in wordSet:res.append(q)
            elif q.lower() in hash:res.append(hash[q.lower()])
            else:
                res.append(hash1.get(vovleEnc(q.lower()),""))
        return res
