class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l_s = ""
        for i in words:
            l_s += i
            l_s += " "
        ans = []
        print(f"this is the long string:",l_s)
        for i in words:
            dummy = l_s.replace(i,"")
            print(i)
            print(dummy)
            if len(dummy) < len(l_s)-len(i):
                ans.append(i)
        return ans