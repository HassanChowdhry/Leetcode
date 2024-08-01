// https://leetcode.com/problems/encode-and-decode-strings

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = 'µ'.join(strs)
        return enc

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        deco = s.split('µ')
        return deco
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))