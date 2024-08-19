class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i in strs:
            s += str(len(i))+"#"+i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        l = 0
        r = 0 
        while r<len(s):
            if s[r] == "#":
                len_wrd = int(s[l:r])
                word = s[r+1:r+1+(len_wrd)]
                res.append(word)
                r = r+len_wrd+1
                l = r
            r += 1
        return res
        

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))