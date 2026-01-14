from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            cur_res = ""
            if i % 3 == 0:
                cur_res += "Fizz"
            if i % 5 == 0:
                cur_res += "Buzz"
            if not cur_res:
                result.append(str(i))
            else:
                result.append(cur_res)
        return result