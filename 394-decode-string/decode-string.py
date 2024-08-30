class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i== ']':
                cur_s = ""
                while stack:
                    ch = stack.pop()
                    if ch == "[":
                        break
                    cur_s += ch
                cur_digit = ""
                while stack:
                    di = stack.pop()
                    if di.isdigit():
                        cur_digit += di
                    else:
                        stack.append(di)
                        break
                cur_digit = cur_digit[::-1]
                if not cur_digit:
                    cur_digit = 1
                else:
                    cur_digit = int(cur_digit)
                stack.append(cur_s*cur_digit)
            else:
                stack.append(i)
        res = ""
        for i in stack:
            res += i[::-1]
        return res












        # if '[' not in s:
        #     return s
        # index = s.find('[')
        # number = ''
        # i = index - 1
        # while i >= 0 and s[i].isdigit():
        #     number = s[i] + number
        #     i -= 1
        # num_start_index = i + 1
        # brackets = 1  # Start with 1 as we are already at one open bracket
        # start = index
        # for i in range(index + 1, len(s)):
        #     if s[i] == '[':
        #         brackets += 1
        #     elif s[i] == ']':
        #         brackets -= 1
        #         if brackets == 0:
        #             end = i
        #             break
        # new_string = ''
        # for i in range(int(number)):
        #     new_string += s[start+1:end]
        
        # return self.decodeString(s[:num_start_index] + new_string + s[end+1:])
