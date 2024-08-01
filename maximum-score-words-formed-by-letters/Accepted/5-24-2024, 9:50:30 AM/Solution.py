// https://leetcode.com/problems/maximum-score-words-formed-by-letters

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        N = len(words)

        mx = []
        freq = [0 for i in range(26)]
        subset = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        def is_valid_word(subset):
            for c in range(26):
                if freq[c] < subset[c]:
                    return False
            
            return True
        
        def backtrack(n, words, score, subset, sc):
            if n == -1:
                mx.append(sc)
                return
           
            backtrack(n - 1, words, score, subset, sc)

            L = len(words[n])
            for i in range(L):
                c = ord(words[n][i]) - 97
                subset[c] += 1
                sc += score[c]

            if is_valid_word(subset):
                backtrack(n - 1, words, score, subset, sc)
                
            for i in range(L):
                c = ord(words[n][i]) - 97
                subset[c] -= 1
                sc -= score[c]

        backtrack(N - 1, words, score, subset, 0)

        return max(mx)