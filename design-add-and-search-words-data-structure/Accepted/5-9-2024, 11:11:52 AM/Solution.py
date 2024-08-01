// https://leetcode.com/problems/design-add-and-search-words-data-structure

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(root, idx):
            if idx>=n:
                return root.end

            c = word[idx]
            if c != '.' and c not in root.children:
                return False

            take = False
            if c in root.children:
                take = take or dfs(root.children[c], idx+1)

            elif c == '.':
                for child in root.children:
                    take = take or dfs(root.children[child], idx+1)
            
            return take # placeholder
        
        return dfs(self.root, 0) # placeholder


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)