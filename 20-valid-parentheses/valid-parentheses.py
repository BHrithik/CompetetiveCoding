class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        concurent_dict = {"{":"}","(":")","[":"]"}
        for i in s:
            if i in concurent_dict.keys():
                stack.append(i)
            elif stack:
                most_recent = stack.pop()
                if concurent_dict[most_recent] == i:
                    continue
                else:
                    return False
            else:
                return False
        return True if not stack else False
