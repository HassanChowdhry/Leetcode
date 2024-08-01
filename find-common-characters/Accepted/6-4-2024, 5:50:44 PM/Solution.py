// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = Counter(words[0])

        for word in words[1:]:
            curr = Counter(word)
            
            int_keys = letters.keys() & curr.keys() 
            for letter in list(letters)[::]:
                if letter not in int_keys:
                    del letters[letter]
                else:
                    letters[letter] = min(letters[letter], curr[letter])
        
        print(letters)
        res = []

        for letter in letters:
            for i in range(letters[letter]):
                res.append(letter)

        return res