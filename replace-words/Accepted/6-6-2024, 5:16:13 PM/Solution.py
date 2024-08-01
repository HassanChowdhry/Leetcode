// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic = set(dictionary)
        s = sentence.split(" ")

        for i, word in enumerate(s):
            r = 1
            while r < len(word):
                root = word[:r]
                if word[:r] in dic:
                    s[i] = root
                    break
                r+=1

        return ' '.join(s)