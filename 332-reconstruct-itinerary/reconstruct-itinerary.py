class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketDict = defaultdict(lambda:[])
        for i in tickets:
            ticketDict[i[0]].append(i[1])
        ticketDict['JFK']
        print(ticketDict)
        for src in ticketDict:
            ticketDict[src].sort(reverse=True)
        path, stack = [], ['JFK']
        while stack:
            while ticketDict[stack[-1]]:
                stack.append(ticketDict[stack[-1]].pop())
            path.append(stack.pop())
        return path[::-1]