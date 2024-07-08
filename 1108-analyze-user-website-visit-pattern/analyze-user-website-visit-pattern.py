class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        history = [(i,j,k) for i,j,k in zip(timestamp,username, website)]
        history.sort()
        users = defaultdict(list)
        patterns = {}
        for time,user,website in history:
            users[user].append(website)
        possibleTuples = defaultdict(int)
        for usr in users:
            webRoutes = set(combinations(users[usr],3))
            for webRoute in webRoutes:
                possibleTuples[webRoute] += 1
        maxVal = max(possibleTuples.values())
        ans = []
        print(possibleTuples)
        for r,val in possibleTuples.items():
            if maxVal == val:
                ans.append(r)
        print(ans)
        ans.sort()
        return ans[0]