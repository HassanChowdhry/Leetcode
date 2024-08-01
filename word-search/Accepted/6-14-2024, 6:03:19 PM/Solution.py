// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        col = len(board[0])
        def backtrack(curr, idx, i, j, visited):
            if i < 0 or j < 0 or i>=rows or j>=col:
                return False
            if (i, j) in visited or board[i][j] != word[idx]:
                return False
            
            curr += word[idx]
            visited.add((i, j))
            if curr == word:
                return True
            
            boolWord = False
            
            boolWord = boolWord or backtrack(curr, idx+1, i-1, j, visited)
            boolWord = boolWord or backtrack(curr, idx+1, i+1, j, visited)
            boolWord = boolWord or backtrack(curr, idx+1, i, j-1, visited)
            boolWord = boolWord or backtrack(curr, idx+1, i, j+1, visited)
            
            if not boolWord:
                visited.remove((i, j))

            return boolWord
        
        isWordInBoard = False
        for i in range(rows):
            for j in range(col):
                if board[i][j]==word[0]:
                    visited = set()
                    isWordInBoard = backtrack("", 0, i, j, visited)
                    if isWordInBoard: return True

        return isWordInBoard