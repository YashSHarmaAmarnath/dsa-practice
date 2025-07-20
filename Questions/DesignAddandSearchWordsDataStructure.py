class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(node,i):
            if i == n:return node.isEnd
            char = word[i]
            if char == '.':
                return any(dfs(child,i+1) for child in node.children.values())
            if char not in node.children:
                return False
            return dfs(node.children[char],i+1)
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
