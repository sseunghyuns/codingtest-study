from collections import defaultdict
'''
https://leetcode.com/problems/reconstruct-itinerary/
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        result = []
        print(graph)
        def dfs(a):
            while graph[a]:
                print(a)
                dfs(graph[a].pop(0))
            result.append(a)   
        
        dfs('JFK')
        print(result[::-1])
        return result[::-1]

    
    
    
    