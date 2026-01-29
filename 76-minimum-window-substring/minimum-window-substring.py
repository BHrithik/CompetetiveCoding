class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "" or s == "":
            return ""
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char,0)+1
        have = 0
        need = len(t_dict)
        l = 0
        s_dict = {}
        res, resLen = [-1,-1], float('inf')
        for r in range(len(s)):
            s_dict[s[r]] = s_dict.get(s[r],0)+1
            if s[r] in t_dict and s_dict[s[r]] == t_dict[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""