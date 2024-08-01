// https://leetcode.com/problems/replace-words

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        
        curr.end = True
    
    def replace(self, word: str) -> str:
        res = ""
        curr = self.root
        for i in word:
            if i not in curr.children:
                return word
            
            res += i

            curr = curr.children[i]
            if curr.end:
                return res
        return res

   

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(" ")
        res = []

        for word in words:
            res.append(trie.replace(word))
        
        return ' '.join(res)