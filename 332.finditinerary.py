# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct the
# itinerary in order and return it.
#
#  All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you should
# return the itinerary that has the smallest lexical order when read as a single
# string.
#
#
#  For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than [
# "JFK", "LGB"].
#
#
#  You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
#
#
#  Example 1:
#
#
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
#
#
#  Example 2:
#
#
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],[
# "ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK",
# "ATL","SFO"] but it is larger in lexical order.
#
#
#
#  Constraints:
#
#
#  1 <= tickets.length <= 300
#  tickets[i].length == 2
#  fromi.length == 3
#  toi.length == 3
#  fromi and toi consist of uppercase English letters.
#  fromi != toi
#
#
#  Related Topics Depth-First Search Graph Eulerian Circuit 👍 5728 👎 1842
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # based on https://www.youtube.com/watch?v=j31ZOupyrAs
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}
        tickets.sort(key=lambda x:x[1])

        # get all possible connection for each destination
        for u,v in tickets:
            if u in self.adj: self.adj[u].append(v)
            else: self.adj[u] = [v]

        self.result = []
        self.dfs("JFK")

        return self.result[::-1]  # reverse to get the result

    def dfs(self, s):
        # if depart city has flight and the flight can go to another city
        while s in self.adj and len(self.adj[s]) > 0:
            v = self.adj[s][0]  # we go to the 1 choice of the city
            self.adj[s].pop(0)  # get rid of this choice since we used it
            self.dfs(v)  # we start from the new airport

        self.result.append(s)  # after append, it will back track to last node, thus the result list is in reversed order


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "JFK"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
        ["ATL", "AAA"],
        ["AAA", "BBB"],
        ["BBB", "ATL"],
    ]
    solution = Solution()
    print(solution.findItinerary(tickets))
