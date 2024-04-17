class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a dictionary to hold all tickets with the source as the key and destinations as the values
        ticketDict = defaultdict(list)
        for src, dst in tickets:
            ticketDict[src].append(dst)
        
        # Sort each destination list in reverse order (for efficient pop from the end)
        for src in ticketDict:
            ticketDict[src].sort(reverse=True)
        
        # The itinerary list
        itinerary = []

        def dfs(airport):
            # Visit all the destinations from the current airport
            while ticketDict[airport]:
                # Get the next destination with the smallest lexical order
                next_airport = ticketDict[airport].pop()
                dfs(next_airport)
            # Append the airport to itinerary after visiting all possible routes from it
            itinerary.append(airport)
        
        # Start the DFS from 'JFK'
        dfs('JFK')

        # Since we add airports in reverse order (post-visiting), we need to reverse the result
        return itinerary[::-1]

# Usage
# sol = Solution()
# result = sol.findItinerary([["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"], ["ATL","JFK"], ["ATL","SFO"]])
# print(result)  # Example output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
