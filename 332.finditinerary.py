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
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort to find the path start at the smallest alphabet
        tickets.sort()
        used = [0] * len(tickets)
        # path start at JFK
        path = ["JFK"]
        results = []
        # flight record dict to check circulate flights
        # flight_records = set()  # store how many times this airport has been landed
        self.backtracking(
            tickets=tickets,
            used=used,
            path=path,
            cur_location='JFK',
            results=results,
            # flight_records=flight_records,
        )
        # return the least lexical order result
        return results[0]

    def backtracking(
        self,
        tickets: List[List[str]],
        used: List[int],
        path: List[str],
        cur_location: str,
        results: List[List[str]],
        # flight_records: set,
    ):
        """
        :param tickets:  ticket list
        :param used: list to mark tickets as used
        :param path: current path
        :param cur_location: current location
        :param results: result tickets
        :return:
        """

        # stop cond: if we used all the tickets, we cannot do further
        # +1 : final destination
        if len(path) == len(tickets) + 1:
            # print(f"add {path} to result")
            results.append(path[:])
            return True  # once we find the first result, it will be the smallest lexical order since we've sorted at first

        # start bfs and dfs all the possible next destination
        for i, ticket in enumerate(tickets):

            # find the ticket which can fly from the current location
            # ticket ex: ["JFK","SFO"]
            # ticket_takeoff_location = ticket[0]
            # ticket_drop_location = ticket[1]
            # print(
            #     f"ticket_takeoff_location == cur_location: {ticket_takeoff_location == cur_location}"
            # )
            # print(
            #     f"ticket_drop_location not in flight_records: {ticket_drop_location in flight_records}"
            # )
            # print(f"ticket_takeoff_location:{ticket_takeoff_location}")
            # print(f"ticket_drop_location:{ticket_drop_location}")
            # print(f"flight_records:{flight_records}")
            # print(f'results: {results}')
            if (
                ticket[0] == cur_location
                and used[i]
                == 0  # not circular, not using flight_records since we will write more to check circular
            ):

                # mark the ticket as used
                used[i] =1
                # proceed the flight
                path.append(ticket[1])
                # # we can take off
                # flight_records = flight_records.union(
                #     set(ticket)
                # )  # add the flight to the traveled record after landing
                # print(tickets)
                # print(used)
                # print(f"current path: {path}")
                # print(f"flight_records: {flight_records}")
                # find another option
                # print("==================================")
                can_reach_destination = self.backtracking(
                    tickets=tickets,
                    used=used,
                    path=path,
                    cur_location=ticket[1],
                    results=results,
                    # flight_records=flight_records
                )
                # back track to find more path
                path.pop()  # pop the last one
                used[i] =0
                # if we can reach the destination, we've found the route
                if can_reach_destination:
                    return True


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
