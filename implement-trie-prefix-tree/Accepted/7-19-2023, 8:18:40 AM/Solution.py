// https://leetcode.com/problems/implement-trie-prefix-tree

# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict

class TrieNode:
  def __init__(self):
    self.children = defaultdict(TrieNode)
    self.endOfWord: bool = False
  
class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  # Time O(n), Space O(n)
  def insert(self, word: str) -> None:
    curr = self.root
    
    for c in word:
      curr = curr.children[c]
      
    curr.endOfWord = True
  
  # Time O(n), Space O(1)
  def search(self, word: str) -> bool:
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      
      curr = curr.children[c]
      
    return curr.endOfWord
      
  # Time O(n), Space O(1)
  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      
      curr = curr.children[c]
      
    return True