// https://leetcode.com/problems/encode-and-decode-tinyurl

class Codec:
    def __init__(self):
        self.map = {}
        self.i = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.map[self.i] = longUrl
        res = f"http://url.com/{self.i}"
        self.i+=1
        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx = int(shortUrl[15:])
        return self.map[idx]

        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))