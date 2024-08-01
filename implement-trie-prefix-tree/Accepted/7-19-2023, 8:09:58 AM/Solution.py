// https://leetcode.com/problems/implement-trie-prefix-tree

# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord: bool = False
  
class Trie:
  def __init__(self):
    self.root = TrieNode()
      
  def insert(self, word: str) -> None:
    curr = self.root
    
    for i, c in enumerate(word):
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
      
      if i == len(word) - 1:
        curr.endOfWord = True
      
  def search(self, word: str) -> bool:
    curr = self.root
    for i, c in enumerate(word):
      if c not in curr.children:
        return False
      
      curr = curr.children[c]
      
      if i == len(word) - 1 and not curr.endOfWord:
        return False
      
    return True
      

  def startsWith(self, prefix: str) -> bool:
    curr = self.root
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
      
    return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)