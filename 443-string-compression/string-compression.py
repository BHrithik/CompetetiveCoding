class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
        # s = []
        # for i in range(0,len(chars)):
        #     count = 1
        #     for j in range(i+1,len(chars)):
        #         if chars[i] == chars[j]:
        #             count = count+1

        #     if count == 1:
        #         s.append(chars[i])
        #     else:
        #         s.append(chars[i])
        #         for l in list(str(count)):
        #             s.append(l)
        # print(s)
        # return len(s)
    
                                

        