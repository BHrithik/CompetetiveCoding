class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = list(senate)
        rs = deque([])
        ds = deque([])
        n = len(senators)
        for index, val in enumerate(senators):
            if val == "R":
                rs.append(index)
            if val == "D":
                ds.append(index)
        while rs and ds:
            r_v = rs.popleft()
            d_v = ds.popleft()
            if r_v < d_v:
                rs.append(r_v+n)
            else:
                ds.append(d_v+n)
        return "Radiant" if rs else "Dire"