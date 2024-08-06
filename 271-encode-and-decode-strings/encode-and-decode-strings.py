class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i in strs:
            s += "hrithik"+i
        print(s)
        return s
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = s.split('hrithik')
        return n[1:]
        # for i in range(0,len(s)):
        #     num = ""
        #     if s[i] == "#":
        #         numstart = i+1
        #         while s[numstart].isalpha()


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))