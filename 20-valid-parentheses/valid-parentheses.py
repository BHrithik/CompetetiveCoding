class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        concurent_dict = {"{":"}","(":")","[":"]"}
        for i in s:
            if i in concurent_dict.keys():
                print(f"Adding {i} to stack")
                stack.append(i)
            elif stack:
                most_recent = stack.pop()
                print(f"Checking if most recent in stack i.e. {most_recent} if comlimented with {i}")
                if concurent_dict[most_recent] == i:
                    continue
                else:
                    return False
            else:
                return False
        return True if not stack else False
