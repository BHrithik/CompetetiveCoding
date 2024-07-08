class Solution:
    def minimumKeypresses(self, s: str) -> int:
        cn = Counter(s)
        keys = defaultdict(list)
        count = 0
        press_once = 9
        press_twice = 9
        press_thrice = 9
        values = list(cn.items())
        values.sort(key=lambda x : -x[1])
        for i in values:
            if press_once > 0:
                count += 1 * i[1]
                press_once -= 1
            elif press_twice > 0:
                count += 2 * i[1]
                press_twice -= 1
            else:
                count += 3 * i[1]
        return count

        

