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
        res,i = [],0
        while i<len(s):
            j = i
            while s[j]!="#":
                j += 1
            num = int(s[i:j])
            j = j+1 ## first letter
            i = num+j ## start of next letter
            res.append(s[j:i])
        return res


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))